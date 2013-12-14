from direct.showbase import DirectObject
class KeyListener(DirectObject.DirectObject):
  
  a = False;
  w = False;
  s = False;
  d = False;
  space = False
  i = False;
  k = False;
  j = False;
  l = False;
  
  def __init__(self):
    self.accept('a', self.ahold)
    self.accept('a-up', self.arelease)
    self.accept('w', self.whold)
    self.accept('w-up', self.wrelease)
    self.accept('s', self.shold)
    self.accept('s-up', self.srelease)
    self.accept('d', self.dhold)
    self.accept('d-up', self.drelease)
    self.accept('i', self.ihold)
    self.accept('i-up', self.irelease)
    self.accept('k', self.khold)
    self.accept('k-up', self.krelease)
    self.accept('j', self.jhold)
    self.accept('j-up', self.jrelease)
    self.accept('l', self.lhold)
    self.accept('l-up', self.lrelease)
    self.accept('space', self.spacehold)
    self.accept('space-up', self.spacerelease)
    
  def ahold(self):
    self.a = True
    
  def arelease(self):
    self.a = False
                
                
  def shold(self):
      self.s = True
    
  def srelease(self):
    self.s = False

  def whold(self):
    self.w = True
    
  def wrelease(self):
    self.w = False
                
  def dhold(self):
    self.d = True
    
  def drelease(self):
    self.d = False
                
  def ihold(self):
      self.i = True
    
  def irelease(self):
    self.i = False
 
  def lhold(self):
      self.l = True
    
  def lrelease(self):
    self.l = False

  def jhold(self):
    self.j = True
    
  def jrelease(self):
    self.j = False
                
  def khold(self):
    self.k = True
    
  def krelease(self):
    self.k = False
                
  def spacehold(self):
    self.space = True
    
  def spacerelease(self):
    self.space = False
                