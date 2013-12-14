'''
Created on 23/01/2011

@author: Will
'''
class Car():
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
        
        
    def goForward(self):
        self.jointfr.addTorques(1,2000)
        self.jointfl.addTorques(1,2000)
        
    def goBackwards(self):
        self.jointfr.addTorques(1,-2000)
        self.jointfl.addTorques(1,-2000)
        
    def turnLeft(self):
        self.jointfr.addTorques(0,-4000)
        self.jointfl.addTorques(0,4000)
        self.jointrr.addTorques(0,-4000)
        self.jointrl.addTorques(0,4000)
        
        
    def turnRight(self):
        self.jointfr.addTorques(0,4000)
        self.jointfl.addTorques(0,-4000)
        self.jointrr.addTorques(0,4000)
        self.jointrl.addTorques(0,-4000)
        