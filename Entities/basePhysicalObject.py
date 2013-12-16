__author__ = 'Will'

from pandac.PandaModules import  LVector3f

class BasePhysicalObject():
    def __init__(self,model,bulletnode):
        self.model = model
        self.bullet_node = bulletnode
        self.starting_position = self.bullet_node.getTransform()
        self.panda_node= render.attachNewNode(self.bullet_node)
        self.model.reparentTo(self.panda_node)

    def get_pos(self):
        return self.bullet_node.getTransform().get_pos()

    def reset_pos(self):
        self.bullet_node.clearForces()
        self.bullet_node.setLinearVelocity(LVector3f(0, 0, 0))
        self.bullet_node.setAngularVelocity(LVector3f(0, 0, 0))
        self.bullet_node.setTransform(self.starting_position)

    def reparentTo(self, target):
        self.panda_node.reparentTo(target)


    def set_starting_pos(self, x, y, z):
        self.starting_position.set_pos(LVector3f(x,y,z))
