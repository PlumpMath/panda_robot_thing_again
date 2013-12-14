'''
Created on 30/07/2009

@author: will
'''
from direct.directbase import DirectStart
from direct.showbase.Loader import Loader
from keyListener import KeyListener
from pandac.PandaModules import OdeBody, OdeMass, OdeSphereGeom, BitMask32, OdeBoxGeom

from random import randint, random
from myModel import MyModel


class ModelCreator():
    
    def createSphere(self,world,space,density = 1,scale = 1):
        sphere = loader.loadModel("smiley.egg")
        sphere.setPos(0, 0, 10)
        #sphere.setColor(0.7, 0.4, 0.4)
        # create body
        sphere.setScale(scale)
        body = OdeBody(world)
        M = OdeMass()
        M.setSphere(density, scale)
        body.setMass(M)
        body.setPosition(sphere.getPos(render))
        body.setQuaternion(sphere.getQuat(render))
        global player
        player = body
        bodyNP = sphere.copyTo(render)
        bodyNP.setColor(random(), random(), random(), 1)

        bodyaGeom = OdeSphereGeom(space,scale)
        bodyaGeom.setCollideBits(BitMask32(0x00000001))
        bodyaGeom.setCategoryBits(BitMask32(0x00000001))
        bodyaGeom.setBody(body)
        
        model = MyModel()
        model.body = body
        model.model = bodyNP
        return model



    def createBox(self,world,space,density = 10, scale = (1,1,1)):
        # Setup the geometry
        box = loader.loadModel("box.egg")
        
        # Make sure its center is at 0, 0, 0 like OdeBoxGeom
        box.setPos(-.5, -.5, -.5)
        box.flattenLight() # Apply transform
        box.setScale(scale)

        
        boxNP = box.copyTo(render)
        #boxNP.setPos(randint(-10, 10), randint(-10, 10), 10 + random())
        boxNP.setColor(random(), random(), random(), 1)
        #boxNP.setHpr(randint(-45, 45), randint(-45, 45), randint(-45, 45))
        # Create the body and set the mass
        boxBody = OdeBody(world)
        M = OdeMass()
        M.setBox(density,scale[0],scale[1],scale[2])
        boxBody.setMass(M)
        boxBody.setPosition(boxNP.getPos(render))
        boxBody.setQuaternion(boxNP.getQuat(render))
        # Create a BoxGeom
        boxGeom = OdeBoxGeom(space,scale[0],scale[1],scale[2])
        boxGeom.setCollideBits(BitMask32(0x00000001))
        boxGeom.setCategoryBits(BitMask32(0x00000001))
        boxGeom.setBody(boxBody)
        
        model = MyModel()
        model.body = boxBody
        model.model = boxNP


        return model

    def createCar(self,world,space,density = 10):
        # Setup the geometry
        box = loader.loadModel("box.egg")
        scale = 4
        box.setScale(scale)
        min, max = box.getTightBounds()
        size = max-min
        center = (min + max)/2 
        print size
        # Make sure its center is at 0, 0, 0 like OdeBoxGeom
        box.setPos(-.5*scale, -.5*scale, -.2*scale)
        box.flattenLight() # Apply transform
        box.setTextureOff()
        
        boxNP = box.copyTo(render)
        #boxNP.setPos(randint(-10, 10), randint(-10, 10), 10 + random())
        boxNP.setColor(random(), random(), random(), 1)
        #boxNP.setHpr(randint(-45, 45), randint(-45, 45), randint(-45, 45))
        # Create the body and set the mass
        boxBody = OdeBody(world)
        M = OdeMass()
        M.setBox(density,size.getX(),size.getY(),size.getZ())
        boxBody.setMass(M)
        boxBody.setPosition(boxNP.getPos(render))
        boxBody.setQuaternion(boxNP.getQuat(render))
        # Create a BoxGeom
        boxGeom = OdeBoxGeom(space,size.getX(),size.getY(),size.getZ())
        boxGeom.setCollideBits(BitMask32(0x00000001))
        boxGeom.setCategoryBits(BitMask32(0x00000001))
        boxGeom.setBody(boxBody)
        
        model = MyModel()
        model.body = boxBody
        model.model = boxNP
        model.size = size
        model.center = center
        return model



    def createQuadro(self,world,space,density = 10):
        # Setup the geometry
        box = loader.loadModel("box.egg")
        scale = 1
        box.setScale(scale)
        min, max = box.getTightBounds()
        size = max-min
        center = (min + max)/2 
        print size
        # Make sure its center is at 0, 0, 0 like OdeBoxGeom
        box.setPos(-.5*scale, -.5*scale, -.2*scale)
        box.flattenLight() # Apply transform
        box.setTextureOff()
        
        boxNP = box.copyTo(render)
        #boxNP.setPos(randint(-10, 10), randint(-10, 10), 10 + random())
        boxNP.setColor(random(), random(), random(), 1)
        #boxNP.setHpr(randint(-45, 45), randint(-45, 45), randint(-45, 45))
        # Create the body and set the mass
        boxBody = OdeBody(world)
        M = OdeMass()
        M.setBox(density,size.getX(),size.getY(),size.getZ())
        boxBody.setMass(M)
        boxBody.setPosition(boxNP.getPos(render))
        boxBody.setQuaternion(boxNP.getQuat(render))
        # Create a BoxGeom
        boxGeom = OdeBoxGeom(space,size.getX(),size.getY(),size.getZ())
        boxGeom.setCollideBits(BitMask32(0x00000001))
        boxGeom.setCategoryBits(BitMask32(0x00000001))
        boxGeom.setBody(boxBody)
        
        model = MyModel()
        model.body = boxBody
        model.model = boxNP
        model.size = size
        model.center = center
        return model


