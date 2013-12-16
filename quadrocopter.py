'''
Created on 23/01/2011

@author: Will
'''
from pandac.PandaModules import Vec2D , VBase3, LMatrix3, LVector3f
from panda3d.bullet import BulletRigidBodyNode
import libpanda
import math
import keyListener
import modelCreator

BASE = 35
DIFFERENTIAL = 1000


class Quadrocopter():
    def __init__(self,world):
        self.key_listener = keyListener.get_instance()
        self.creator = modelCreator.get_instance()
        self.node, self.model = self.creator.createBox()
        self.starting_position = self.node.getTransform()
        self.np = render.attachNewNode(self.node)
        self.np.setPos(0, 0, 4)
        self.model.reparentTo(self.np)



    def get_pos(self):
        #print dir(self.node.getTransform())
        #print self.node.getTransform().getPos()
        return self.node.getTransform().getPos()

    def reset_pos(self):
        self.node.clearForces()
        self.node.setLinearVelocity(LVector3f(0, 0, 0))
        self.node.setAngularVelocity(LVector3f(0, 0, 0))
        self.node.setTransform(self.starting_position)

        #print self.objects
        pass

    def goUp(self):
        self.node.setActive(True)
        self.node.applyCentralForce(LVector3f(0,0,100))
    
    def goForward(self):
        
        self.rlwheel.body.addRelForce(0,0,100)
        self.rrwheel.body.addRelForce(0,0,100)

    def goBackwards(self):
        
        self.frwheel.body.addRelForce(0,0,100)        
        self.flwheel.body.addRelForce(0,0,100)
        
    def turnLeft(self):
        self.rlwheel.body.addRelForce(0,0,100)        
        self.flwheel.body.addRelForce(0,0,100)
        
    def turnRight(self):
        self.rrwheel.body.addRelForce(0,0,100)        
        self.frwheel.body.addRelForce(0,0,100)

    def tick(self):
        if self.key_listener.keys['i']:
            self.goForward()
        if self.key_listener.keys['k']:
            self.goBackwards()
        if self.key_listener.keys['l']:
            self.turnRight()
        if self.key_listener.keys['j']:
            self.turnLeft()
        if self.key_listener.keys['space']:
            self.goUp()
        if self.key_listener.keys['x']:
            self.reset_pos()