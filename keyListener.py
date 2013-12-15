from direct.showbase import DirectObject



instance = None


def get_instance():
    global instance
    if instance:
        return instance
    else:
        global instance
        instance = KeyListener()
        return instance


class KeyListener(DirectObject.DirectObject):

    _letras = "abcdefghijklmnopqrstuvwxyz1234567890"
    _keys = ['space', 'tab']
    for letra in _letras:
        _keys.append(letra)

    keys = {}

    for key in _keys:
        keys[key] = False

    def set(self, key):
        self.keys[key.split('-')[0]] = True

    def unset(self, key):
        self.keys[key.split('-')[0]] = False

    def __init__(self):
        for key in self._keys:
            self.accept(key, self.set,   [key])
            self.accept(key+"-up", self.unset, [key])



