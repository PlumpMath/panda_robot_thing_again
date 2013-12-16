__author__ = 'Will'


class Map():
    def __init__(self,model,bullet_node):
        self.model = model
        self.bullet_node = bullet_node
        self.bullet_node.setGravity(False)
        self.starting_position = self.bullet_node.getTransform()
        self.panda_node= render.attachNewNode(self.bullet_node)
        self.model.reparentTo(self.panda_node)
