__author__ = 'Will'

from pandac.PandaModules import Quat, OdeWorld, OdeSimpleSpace, OdeJointGroup
from direct.gui.OnscreenText import OnscreenText

from keyListener import KeyListener
from libpanda import Mat3
from panda3d.bullet import BulletWorld
import modelCreator
from Entities.quadrocopter import Quadrocopter
from shadowManager import ShadowManager


chassis = None
camera_targets = []
sMgr = None



from panda3d.bullet import BulletDebugNode

#debugNode = BulletDebugNode('Debug')
#debugNode.showWireframe(True)
#debugNode.showConstraints(True)
#debugNode.showBoundingBoxes(True)
#debugNode.showNormals(True)
#debugNP = render.attachNewNode(debugNode)
#debugNP.show()


def setup_shadows():
    global sMgr
    sMgr = ShadowManager(render)
    sMgr.setAmbient(0.2)     # Most of these five are the default
    sMgr.setHardness(20)     # values so it was kinda unnecessary to
    sMgr.setFov(40)          # set them explicitly but I wanted to
    sMgr.setNearFar(10, 120) # show how to set them anyway.
    sMgr.light.setPos(10, -10, 100)
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
    world = BulletWorld()
    # world.setDebugNode(debugNP.node())
    world.setGravity(0, 0, -9.81)


def physics_tick(task):
    dt = globalClock.getDt()
    world.doPhysics(dt)
    return task.cont


def update_camera():
    for target in camera_targets:
        posdiff = target.get_pos() - base.cam.getPos()
        if posdiff.length() > 40:
            posdiff.setZ(0)
            newPos = base.cam.getPos() + posdiff*0.01
            newPos.setZ(15)
            base.cam.setPos(newPos)

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
    physics_tick(task)
    return task.cont


if __name__ == "__main__":
    setup_physics()
    setup_shadows()
    setup_camera()
    modelcreator = modelCreator.get_instance(world)
    key_listener = KeyListener()
    vehicle = Quadrocopter(world)
    camera_targets.append(vehicle)
    #table = modelcreator.createGround()
    map = modelcreator.createMap()
    sMgr.flagUntexturedObject(map.panda_node)

    text = OnscreenText("")

    taskMgr.doMethodLater(0.5, simulationTask, "Physics Simulation")
    run()



