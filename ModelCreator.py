'''
Created on 30/07/2009

@author: will
'''
from direct.directbase import DirectStart
from direct.showbase.Loader import Loader
from pandac.libpandaModules import Vec3
from pandac.PandaModules import Texture
from pandac.PandaModules import GeoMipTerrain
from Entities.basePhysicalObject import BasePhysicalObject
from Entities.map import Map
from panda3d.bullet import BulletRigidBodyNode, BulletBoxShape, BulletSphereShape, BulletPlaneShape

from panda3d.core import Filename
from panda3d.core import PNMImage
from panda3d.bullet import BulletHeightfieldShape
from panda3d.bullet import ZUp

instance = None


def get_instance(world=None):
    global instance
    if instance:
        return instance
    else:
        print "created"
        instance = ModelCreator(world)
        return instance


class ModelCreator():
    def __init__(self, world=None):
        if world:
            self.world = world

    def createSphere(self, world, mass=1, scale=1):
        shape = BulletSphereShape(scale)
        node = BulletRigidBodyNode('Sphere')
        node.setMass(mass)
        node.addShape(shape)
        #np = render.attachNewNode(node)
        #np.setPos(0, 0, 4)
        world.attachRigidBody(node)
        model = loader.loadModel('models/smiley.egg')

        model.setScale(scale)
        #model.setPos(-scale[0],-scale[1],-scale[2])
        model.flattenLight()
        #model.reparentTo(np)
        return BasePhysicalObject(model,node)


    def createBox(self, mass=5, scale=(1, 1, 1)):
        shape = BulletBoxShape(Vec3(*scale))
        node = BulletRigidBodyNode('Box')
        node.setMass(mass)
        node.addShape(shape)
        #np = render.attachNewNode(node)
        #np.setPos(0, 0, 2)
        self.world.attachRigidBody(node)
        model = loader.loadModel('models/box.egg')
        scalex2 = []
        for item in scale:
            scalex2.append(item * 2)
        model.setScale(*scalex2)
        model.setPos(-scale[0], -scale[1], -scale[2])
        model.flattenLight()
        #model.reparentTo(np)
        return BasePhysicalObject(model,node)

    def createMap(self):

        height = 10.0
        img = PNMImage(Filename('resources/map1.bmp'))
        shape = BulletHeightfieldShape(img, height, ZUp)
        node = BulletRigidBodyNode('Map')
        node.setMass(99999999)
        node.addShape(shape)
        self.world.attachRigidBody(node)
        offset = img.getXSize() / 2.0 - 0.5
        terrain = GeoMipTerrain('terrain')
        terrain.setHeightfield(img)
        terrainNP = terrain.getRoot()
        terrainNP.setSz(height)
        terrainNP.setPos(-offset, -offset, -height / 2.0)
        #terrain.setColorMap('resources/map1color.bmp')
        terrain.setAutoFlatten(GeoMipTerrain.AFMOff)
        terrain.generate()

        return Map(terrainNP,node)



    def createGround(self):
        shape = BulletPlaneShape(Vec3(0, 0, 1), 1)
        node = BulletRigidBodyNode('Ground')
        node.addShape(shape)
        np = render.attachNewNode(node)
        np.setPos(0, 0, -2)
        self.world.attachRigidBody(node)

        table = loader.loadModel("tableplane.egg")
        table.reparentTo(np)
        tableTex = loader.loadTexture("tree-bark-89a.jpg")
        tableTex.setMinfilter(Texture.FTLinearMipmapLinear) # Enable texture mipmapping
        table.setTexture(tableTex)
        table.setPos(0,0,-0.1)
        table.setScale(2) # fucks the shadows


