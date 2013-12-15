'''
Created on 23/01/2011

@author: Will
'''
from pandac.PandaModules import Vec2D , VBase3, LMatrix3
import libpanda
import math
import keyListener

BASE = 35
DIFFERENTIAL = 1000
class Quadrocopter():
    def __init__(self):
        self.key_listener = keyListener.get_instance()
        self.jointrr = None
        self.rrwheel = None
        self.jointrl = None
        self.rlwheel = None
        self.jointfr = None
        self.frwheel = None
        self.chassiM = None
        self.jointfl = None
        self.flwheel = None
        self.objects = None

    def get_renderable_bodies(self):
        lista = []
        lista.extend([self.rrwheel.model,self.frwheel.model,self.flwheel.model,self.rlwheel.model,self.chassiM.model])
        return lista

    def get_pos(self):
        return self.chassiM.model.get_pos()

    def setRRWheel(self,jointrr,rrwheel):
        self.jointrr = jointrr
        self.rrwheel = rrwheel
        
    def setRLWheel(self,jointrl,rlwheel):
        self.jointrl = jointrl
        self.rlwheel = rlwheel
        
    def setFRWheel(self,jointfr,frwheel):
        self.jointfr = jointfr
        self.frwheel = frwheel
    
    def setModel(self, chassiM):
        self.chassiM = chassiM
    
    def setObjects(self,objects):
        self.objects = objects
        
    def setFLWheel(self,jointfl,flwheel):
        self.jointfl = jointfl
        self.flwheel = flwheel
               
    
    def getrlpos(self):
        return self.rlwheel.body.getPosition()
    
    def getrrpos(self):
        return self.rrwheel.body.getPosition()
    
    def getflpos(self):
        return self.flwheel.body.getPosition()
    
    def getfrpos(self):
        return self.frwheel.body.getPosition()

    def getYawVel(self):
        return self.chassiM.body.getAngularVel()[2]
    
    def getPitchVel(self):
        return  - self.chassiM.body.getAngularVel()[0]
        
    def getRollVel(self):        
        return self.chassiM.body.getAngularVel()[1]
        
        
    def getDistance(self,a,b):
        x = a[0] - b[0]
        y = a[1] - b[1]
        z = a[2] - b[2]
        #r = math.fabs(math.sqrt(x*x + y*y + z*z))
        r = math.sqrt(x*x + y*y + z*z)
        if r > 6:
            return 6
        else:
            return r

    def set_pos(self,x,y,z,roll,pitch,yaw):
        #print self.objects
        for i in self.objects:
            #i[1].setPosition(0,0,3)
            i[1].setLinearVel(0,0,0)
            i[1].set_angular_vel(0,0,0)
            i[1].set_rotation(LMatrix3.ident_mat())


        self.chassiM.body.setPosition(0,0,3)
        self.chassiM.body.setLinearVel(0,0,0)
        # self.chassiM.body.set_angular_vel(0,0,0)
        # self.chassiM.body.set_rotation(LMatrix3.ident_mat())
        #print dir(self.chassiM.body)

    
        
    def getRRThrust(self):
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()
        if roll < 0 and rollVel < 0:
            base = base - DIFFERENTIAL * roll
            print "rr on"
        if yaw < 0 and yawVel < 0:
            base = base + DIFFERENTIAL * yaw
        return base
        
    def getRLThrust(self):     
        
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()         
        if roll > 0 and rollVel > 0:
            base = base - DIFFERENTIAL * roll
            pass
        if yaw < 0 and yawVel < 0:
            base = base + DIFFERENTIAL * yaw
        
        return base
            
    def getFRThrust(self):             
        
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()         
        if roll < 0 and rollVel < 0:
            base = base + DIFFERENTIAL * roll
            pass
        if yaw > 0 and yawVel > 0:
            base = base - DIFFERENTIAL * yaw
        
        return base




    def getFLThrust(self):        
             
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()         
        if roll > 0 and rollVel > 0:
            base = base - DIFFERENTIAL * roll
            pass
        if yaw > 0 and yawVel > 0:
            base = base - DIFFERENTIAL * yaw
        
        return base

    def goUp(self):
        self.rlwheel.body.addRelForce(0,0,100)
        self.rrwheel.body.addRelForce(0,0,100)
        self.frwheel.body.addRelForce(0,0,100)        
        self.flwheel.body.addRelForce(0,0,100)
    
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
            self.set_pos(0,0,0,0,0,0)