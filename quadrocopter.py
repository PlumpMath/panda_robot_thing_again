'''
Created on 23/01/2011

@author: Will
'''
from pandac.PandaModules import Vec2D , VBase3
import libpanda
import math
 
BASE = 35
DIFERENTIAL = 1000
class Quadrocopter():
    def __init__(self):
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
        
    
        
    def getRRThrust(self):
        
        
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()
        if roll < 0 and rollVel < 0:
            base = base - DIFERENTIAL * roll
            print "rr on"
        if yaw < 0 and yawVel < 0:
            base = base + DIFERENTIAL * yaw
        return base
        
    def getRLThrust(self):     
        
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()         
        if roll > 0 and rollVel > 0:
            base = base - DIFERENTIAL * roll
            pass
        if yaw < 0 and yawVel < 0:
            base = base + DIFERENTIAL * yaw
        
        return base
            
    def getFRThrust(self):             
        
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()         
        if roll < 0 and rollVel < 0:
            base = base + DIFERENTIAL * roll
            pass
        if yaw > 0 and yawVel > 0:
            base = base - DIFERENTIAL * yaw
        
        return base
    
    def getFLThrust(self):        
             
        
        yaw = self.getYaw()
        yawVel = self.getYawVel()
        roll = self.getRoll()
        base = BASE    
        rollVel = self.getRollVel()         
        if roll > 0 and rollVel > 0:
            base = base - DIFERENTIAL * roll
            pass
        if yaw > 0 and yawVel > 0:
            base = base - DIFERENTIAL * yaw
        
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
        