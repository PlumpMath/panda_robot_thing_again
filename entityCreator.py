'''
Created on 23/01/2011

@author: Will
'''

from pandac.PandaModules import Texture , OdePlaneGeom, Vec4, BitMask32, OdeHinge2Joint
from ModelCreator import ModelCreator
from quadrocopter import Quadrocopter
from car import Car
class EntityCreator():
    
    def __init__(self,space,world):
        self.space = space
        self.world = world
    
    def createGround(self):
        table = loader.loadModel("tableplane.egg")
        table.reparentTo(render)
        tableTex = loader.loadTexture("tree-bark-89a.jpg")
        tableTex.setMinfilter(Texture.FTLinearMipmapLinear) # Enable texture mipmapping
        table.setTexture(tableTex)
        table.setPos(0,0,-0.1)
        table.setScale(2) # fucks the shadows
        groundGeom = OdePlaneGeom(self.space, Vec4(0, 0, 1, 0))
        groundGeom.setCollideBits(BitMask32(0x00000001))
        groundGeom.setCategoryBits(BitMask32(0x00000001))
        return table
    
    def createCar(self):        
        CFM1 = 0.002
        CFM0 = 0.003
        FMAX0 = 0

        objects = []
        modelcreator = ModelCreator()
        space = self.space
        world = self.world
        playerM = modelcreator.createSphere(world,space)
        player = playerM.body
        objects.append([playerM.model,playerM.body])
        
        frwheel = modelcreator.createSphere(world,space,density = 10)
        
        objects.append([frwheel.model,frwheel.body])
        flwheel = modelcreator.createSphere(world,space,density = 10)
        objects.append([flwheel.model,flwheel.body])
        rrwheel = modelcreator.createSphere(world,space,density = 10)
        objects.append([rrwheel.model,rrwheel.body])
        rlwheel = modelcreator.createSphere(world,space,density = 10)
        objects.append([rlwheel.model,rlwheel.body])
        
        chassiM =  modelcreator.createCar(world,space)
        chassiM.density = 10
        chassiM.body.setPosition(0,0,12)
        objects.append([chassiM.model,chassiM.body])
        
        frwheel.body.setPosition(-3,2,10)
        flwheel.body.setPosition(3,2,10)
        rrwheel.body.setPosition(-3,-2,10)
        rlwheel.body.setPosition(3,-2,10)
        playerM.body.setPosition(3,2,20)
        
        jointfr = OdeHinge2Joint(world)
        jointfr.attach(chassiM.body,frwheel.body )
        jointfr.setAnchor(frwheel.body.getPosition())
        jointfr.setAxis1(0,0,1)
        jointfr.setParamFMax(0,FMAX0)
        #jointfr.setParamSuspensionCFM(0,CFM0)
        jointfr.setParamHiStop(0,0)
        jointfr.setParamLoStop(0,0)
        jointfr.setAxis2(1,0,0)
        jointfr.setParamFMax(1,500)
        jointfr.setParamSuspensionCFM(1,CFM1)
        jointfr.setParamStopERP(1,0.8)
        
        jointfl = OdeHinge2Joint(world)
        jointfl.attach(chassiM.body,flwheel.body)
        jointfl.setAnchor(flwheel.body.getPosition())
        jointfl.setAxis1(0,0,1)
        jointfl.setParamFMax(0,FMAX0)
        #jointfl.setParamSuspensionCFM(0,CFM0)
        jointfl.setParamHiStop(0,0)
        jointfl.setParamLoStop(0,0)
        jointfl.setAxis2(1,0,0)
        jointfl.setParamFMax(1,500)
        jointfl.setParamSuspensionCFM(1,CFM1)
        jointfl.setParamStopERP(1,0.8)
        
        jointrl = OdeHinge2Joint(world)
        jointrl.attach(chassiM.body,rlwheel.body)
        jointrl.setAnchor(rlwheel.body.getPosition())
        jointrl.setAxis1(0,0,1)
        jointrl.setParamFMax(0,FMAX0)
        #jointrl.setParamSuspensionCFM(0,CFM0)
        jointrl.setParamHiStop(0,0)
        jointrl.setParamLoStop(0,0)
        jointrl.setAxis2(1,0,0)
        jointrl.setParamFMax(1,500)
        jointrl.setParamSuspensionCFM(1,CFM1)
        jointrl.setParamStopERP(1,0.8)
        
        
        jointrr = OdeHinge2Joint(world)
        jointrr.attach( chassiM.body,rrwheel.body)
        jointrr.setAnchor(rrwheel.body.getPosition())
        jointrr.setAxis1(0,0,1)
        jointrr.setParamFMax(0,FMAX0)
        #jointrr.setParamSuspensionCFM(0,CFM0)
        jointrr.setParamHiStop(0,0)
        jointrr.setParamLoStop(0,0)
        jointrr.setAxis2(1,0,0)
        jointrr.setParamFMax(1,500)
        jointrr.setParamSuspensionCFM(1,CFM1)
        jointrr.setParamStopERP(1,0.8)
        car = Car()
        car.setObjects(objects)
        car.setRRWheel(jointrr,rrwheel)
        car.setRLWheel(jointrl,rlwheel)
        car.setFRWheel(jointfr,frwheel)
        car.setModel(chassiM)
        car.setFLWheel(jointfl,flwheel)
        return car
    
    def createQuadrocopter(self):        
        CFM1 = 0
        CFM0 = 0
        FMAX0 = 0

        objects = []
        modelcreator = ModelCreator()
        space = self.space
        world = self.world
        #playerM = modelcreator.createSphere(world,space)
        #player = playerM.body
        #objects.append([playerM.model,playerM.body])
        
        frwheel = modelcreator.createSphere(world,space,density = 0.1)
        objects.append([frwheel.model,frwheel.body])
        flwheel = modelcreator.createSphere(world,space,density = 0.1)
        objects.append([flwheel.model,flwheel.body])
        rrwheel = modelcreator.createSphere(world,space,density = 0.1)
        objects.append([rrwheel.model,rrwheel.body])
        rlwheel = modelcreator.createSphere(world,space,density = 0.1)
        objects.append([rlwheel.model,rlwheel.body])
        
        chassiM =  modelcreator.createQuadro(world,space)
        chassiM.density = 10
        chassiM.body.setPosition(0,0,12)
        objects.append([chassiM.model,chassiM.body])
        
        frwheel.body.setPosition(-3,3,15)
        flwheel.body.setPosition(3,3,15)
        rrwheel.body.setPosition(-3,-3,15)
        rlwheel.body.setPosition(3,-3,15)
#        playerM.body.setPosition(0,0,20)
        
        jointfr = OdeHinge2Joint(world)
        jointfr.attach(chassiM.body,frwheel.body )
        jointfr.setAnchor(frwheel.body.getPosition())
        jointfr.setAxis1(0,0,1)
        jointfr.setParamFMax(0,FMAX0)
        #jointfr.setParamSuspensionCFM(0,CFM0)
        jointfr.setParamHiStop(0,0)
        jointfr.setParamLoStop(0,0)
        jointfr.setAxis2(1,0,0)
        jointfr.setParamFMax(1,500)
        #jointfr.setParamSuspensionCFM(1,CFM1)
        jointfr.setParamStopERP(1,0.8)
        
        jointfl = OdeHinge2Joint(world)
        jointfl.attach(chassiM.body,flwheel.body)
        jointfl.setAnchor(flwheel.body.getPosition())
        jointfl.setAxis1(0,0,1)
        jointfl.setParamFMax(0,FMAX0)
        #jointfl.setParamSuspensionCFM(0,CFM0)
        jointfl.setParamHiStop(0,0)
        jointfl.setParamLoStop(0,0)
        jointfl.setAxis2(1,0,0)
        jointfl.setParamFMax(1,500)
        #jointfl.setParamSuspensionCFM(1,CFM1)
        jointfl.setParamStopERP(1,0.8)
        
        jointrl = OdeHinge2Joint(world)
        jointrl.attach(chassiM.body,rlwheel.body)
        jointrl.setAnchor(rlwheel.body.getPosition())
        jointrl.setAxis1(0,0,1)
        jointrl.setParamFMax(0,FMAX0)
        #jointrl.setParamSuspensionCFM(0,CFM0)
        jointrl.setParamHiStop(0,0)
        jointrl.setParamLoStop(0,0)
        jointrl.setAxis2(1,0,0)
        jointrl.setParamFMax(1,500)
        #jointrl.setParamSuspensionCFM(1,CFM1)
        jointrl.setParamStopERP(1,0.8)
        
        
        jointrr = OdeHinge2Joint(world)
        jointrr.attach( chassiM.body,rrwheel.body)
        jointrr.setAnchor(rrwheel.body.getPosition())
        jointrr.setAxis1(0,0,1)
        jointrr.setParamFMax(0,FMAX0)
        #jointrr.setParamSuspensionCFM(0,CFM0)
        jointrr.setParamHiStop(0,0)
        jointrr.setParamLoStop(0,0)
        jointrr.setAxis2(1,0,0)
        jointrr.setParamFMax(1,500)
        #jointrr.setParamSuspensionCFM(1,CFM1)
        jointrr.setParamStopERP(1,0.8)
        car = Quadrocopter()
        car.setObjects(objects)
        car.setRRWheel(jointrr,rrwheel)
        car.setRLWheel(jointrl,rlwheel)
        car.setFRWheel(jointfr,frwheel)
        car.setModel(chassiM)
        car.setFLWheel(jointfl,flwheel)
        return car