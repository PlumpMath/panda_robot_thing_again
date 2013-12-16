from direct.directbase import DirectStart
from direct.showbase.Loader import Loader
from predef import *
from keyListener import KeyListener
from libpanda import Mat3
from pandac.PandaModules import  Vec3D, BitMask32, CardMaker, Vec4, Quat, OdeBody, OdeMass, OdeBoxGeom, OdePlaneGeom, OdeWorld,OdeSimpleSpace,OdeJointGroup,OdeSphereGeom, OdeHinge2Joint,Texture
from random import randint, random

from modelCreator import ModelCreator
from direct.gui.OnscreenText import OnscreenText
from shadowManager import ShadowManager
from entityCreator import EntityCreator
chassis = None


def createWorldAndStuff():

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
        objects.append((temp.model, temp.body))


# The task for our simulation'
def simulationTask(task):

    if vehicle != None and vehicle.chassiM != None:
        base.cam.lookAt(vehicle.chassiM.model)
    global text
    text.destroy()
    text = OnscreenText(text = ('fps = '+str(globalClock.getAverageFrameRate())) , pos = (0, 0.9), scale = 0.07)
    
    if(keylistener.space):
        vehicle.goUp()     
    if(keylistener.i):
        vehicle.goForward()                
    if(keylistener.k):
        vehicle.goBackwards()        
    if(keylistener.j):
        vehicle.turnLeft()               
    if(keylistener.l):
        vehicle.turnRight()
        
    space.autoCollide() 
    world.quickStep(globalClock.getDt())
    for np, body in objects:
        np.setPosQuat(render, body.getPosition(), Quat(body.getQuaternion()))
    contactgroup.empty()
    return task.cont
         
        
def createGeneralBoxes():
    for i in range(10):        
        # Setup the geometry
        temp = modelcreator.createBox(world, space)
        temp.body.setPosition(randint(-15,15),randint(-15,15),randint(-15,15))
        objects.append((temp.model, temp.body))


modelcreator = ModelCreator()

text = OnscreenText("")
sMgr = ShadowManager(render)
sMgr.setAmbient(0.2)     # Most of these five are the default
sMgr.setHardness(20)     # values so it was kinda unnecessary to
sMgr.setFov(40)          # set them explicitly but I wanted to
sMgr.setNearFar(10, 100) # show how to set them anyway.
sMgr.light.setPos(10, -10, 50)
sMgr.light.lookAt(0)
#sMgr.light.node().showFrustum()

createWorldAndStuff()
entityCreator = EntityCreator(space,world)
keylistener = KeyListener()
objects = []

vehicle = entityCreator.createQuadrocopter()
objects.extend(vehicle.objects)

table = entityCreator.createGround()

# Set the camera position
#base.disableMouse()
camPivot = render.attachNewNode("cameraPivotPoint")
base.cam.reparentTo(camPivot)
base.camLens.setNearFar(1,1000)
base.camLens.setFov(75)
base.cam.setPos(0,-50,15)
base.cam.lookAt(0,0,0)




for child in vehicle.get_renderable_bodies():
    sMgr.flagTexturedObject(child)
sMgr.flagTexturedObject(table)

taskMgr.doMethodLater(0.5, simulationTask, "Physics Simulation")


run()



