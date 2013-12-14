#!/usr/bin/env python

from pandac.PandaModules import loadPrcFileData
loadPrcFileData("", "prefer-parasite-buffer #f")
#loadPrcFileData("", "show-frame-rate-meter #t")
from direct.directbase import DirectStart

# Import whatever classes are necessary
from pandac.PandaModules import Texture, Vec3, Point3
from direct.interval.IntervalGlobal import Sequence
from sys import exit

# Import the Shadow Manager
from shadowManager import ShadowManager

class World(object):
  def __init__(self):
    
    # Make a way out of here!
    base.accept("escape", exit)

    # Initiate the shadows
    self.sMgr = ShadowManager(render)
    self.sMgr.setAmbient(0.2)     # Most of these five are the default
    self.sMgr.setHardness(20)     # values so it was kinda unnecessary to
    self.sMgr.setFov(40)          # set them explicitly but I wanted to
    self.sMgr.setNearFar(10, 100) # show how to set them anyway.

    # Create the 'table'
    self.table = loader.loadModel("tableplane.egg")
    self.table.reparentTo(render)
    tableTex = loader.loadTexture("tree-bark-89a.jpg")
    tableTex.setMinfilter(Texture.FTLinearMipmapLinear) # Enable texture mipmapping
    self.table.setTexture(tableTex)

    # Load the teapot
    self.teapot = loader.loadModel("teapot")
    self.teapot.setTwoSided(True)
    self.teapot.reparentTo(render)
    # The teapot has no texture, so you have to tell it to the ShadowManager
    # Otherwise the model will turn up black.
    self.sMgr.flagUntexturedObject(self.teapot)

    # Set intervals to move the teapot
    self.teapot.hprInterval(5.0, Vec3.zero(), Vec3(360, 0, 0)).loop()
    Sequence(self.teapot.posInterval(2.0, Point3.zero(), Point3(2, 0, 1)), self.teapot.posInterval(2.0, Point3(2, 0, 1), Point3.zero())).loop()

    # Setup the camera
    base.disableMouse()
    camPivot = render.attachNewNode("cameraPivotPoint")
    base.cam.reparentTo(camPivot)
    base.camLens.setNearFar(1,1000)
    base.camLens.setFov(75)
    base.cam.setPos(-10,-10,15)
    base.cam.lookAt(self.teapot)
    
    # Setup an interval to rotate the camera around camPivot
    camPivot.hprInterval(15.0, Vec3.zero(), Vec3(360, 0, 0)).loop()
    
    # Position the shadow camera
    self.sMgr.light.setPos(0,20,15)
    self.sMgr.light.lookAt(self.teapot)
    self.sMgr.light.node().showFrustum() # Show the frustrum


# Initiate the world class and run!
World();run()

