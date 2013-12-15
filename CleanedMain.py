__author__ = 'Will'

from direct.directbase import DirectStart
from direct.showbase.Loader import Loader
from keyListener import KeyListener
from libpanda import Mat3
from pandac.PandaModules import Quat, OdeWorld, OdeSimpleSpace, OdeJointGroup
from random import randint

from ModelCreator import ModelCreator
from direct.gui.OnscreenText import OnscreenText
from shadowManager import ShadowManager
from entityCreator import EntityCreator
chassis = None
camera_targets = []
sMgr = None


def setup_shadows():
    global sMgr
    sMgr = ShadowManager(render)
    sMgr.setAmbient(0.2)     # Most of these five are the default
    sMgr.setHardness(20)     # values so it was kinda unnecessary to
    sMgr.setFov(40)          # set them explicitly but I wanted to
    sMgr.setNearFar(10, 100) # show how to set them anyway.
    sMgr.light.setPos(10, -10, 50)
    sMgr.light.lookAt(0)


def setup_camera():
    camPivot = render.attachNewNode("cameraPivotPoint")
    base.cam.reparentTo(camPivot)
    base.camLens.setNearFar(1,1000)
    base.camLens.setFov(75)
    base.cam.setPos(0,-50,15)
    base.cam.lookAt(0,0,0)


def setup_physics():
    global world
    global space
    global contactgroup
    world = OdeWorld()
    world.setGravity(0, 0, -9.81)
    # The surface table is needed for autoCollide
    world.initSurfaceTable(1)
    world.setSurfaceEntry(0, 0, 15000, 0.001, 0.9, 0.9, 0.00001, 0.1, 0.002)
    # Create a space and add a contactgroup to it to add the contact joints
    space = OdeSimpleSpace()
    space.setAutoCollideWorld(world)
    contactgroup = OdeJointGroup()
    space.setAutoCollideJointGroup(contactgroup)


def create_general_balls():
    for i in range(10):
        # Setup the geometry
        temp = modelcreator.createSphere(world, space)
        temp.body.setPosition(randint(-15,15),randint(-15,15),randint(10,55))
        physical_objects.append((temp.model, temp.body))

def physics_tick():
    space.autoCollide()
    world.quickStep(globalClock.getDt())
    for np, body in physical_objects:
        np.setPosQuat(render, body.getPosition(), Quat(body.getQuaternion()))
    contactgroup.empty()

def update_camera():
    for target in camera_targets:
        base.cam.lookAt(target.get_pos())
        sMgr.light.lookAt(target.get_pos())

def update_gui():
    global text
    text.destroy()
    text = OnscreenText(text=('fps = '+str(globalClock.getAverageFrameRate())) , pos = (0, 0.9), scale = 0.07)


# The task for our simulation'
def simulationTask(task):
    update_camera()
    update_gui()
    vehicle.tick()
    physics_tick()
    return task.cont


if __name__ == "__main__":
    setup_physics()
    setup_shadows()
    setup_camera()

    entityCreator = EntityCreator(space, world)
    key_listener = KeyListener()
    vehicle = entityCreator.createQuadrocopter()
    camera_targets.append(vehicle)
    table = entityCreator.createGround()

    #############must hide this!############
    physical_objects = []
    physical_objects.extend(vehicle.objects)
    ########################################
    text = OnscreenText("")

    taskMgr.doMethodLater(0.5, simulationTask, "Physics Simulation")
    run()



