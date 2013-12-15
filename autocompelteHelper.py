# -*- coding: UTF-8 -*-

import inspect
from panda3d.core import *
import libpanda, libpandaexpress

from panda3d.fx import *
import libpandafx

from panda3d.dtoolconfig import *
import libp3dtoolconfig

from panda3d.physics import *
import libpandaphysics

from panda3d.direct import *
import libp3direct

from panda3d.egg import *
import libpandaegg

from panda3d.ode import *
import libpandaode

from panda3d.bullet import *
import libpandabullet

from panda3d.vision import *
import libp3vision

#from panda3d.physx import *
#import libpandaphysx

from panda3d.ai import *
import libpandaai

#from panda3d.awesomium import *
#import libp3awesomium

#from panda3d.speedtree import *
#import libpandaspeedtree

from panda3d.rocket import *
import _rocketcore, _rocketcontrols, libp3rocket

BUILD = {
    'fx'           : [libpandafx]
    ,'core'        : [libpanda, libpandaexpress]
    ,"dtoolconfig" : [libp3dtoolconfig]
    ,"physics"     : [libpandaphysics]
    ,"fx"          : [libpandafx]
    ,"direct"      : [libp3direct]
    ,"egg"         : [libpandaegg]
    ,"ode"         : [libpandaode]
    ,"bullet"      : [libpandabullet]
    ,"vision"      : [libp3vision]
#    ,"physx"       : [libpandaphysx]
    ,"ai"          : [libpandaai]
#    ,"awesomium"   : [libp3awesomium]
#    ,"speedtree"   : [libpandaspeedtree]
    ,"rocket"      : [_rocketcore, _rocketcontrols, libp3rocket],
}

indent = '    '
importptrn = 'from panda3d.%s import %s'
skip = [
                'DtoolGetSupperBase',
                'DtoolClassDict'
             ]

def record(t, name, f, noclasses=False, baseIndent=''):
    if name.startswith('__'): return
    if isinstance(t, int):
        f.write('%s%s = int\n\n' % (baseIndent, name))
        return True
    elif isinstance(t, float):
        f.write('%s%s = float\n\n' % (baseIndent, name))
        return True
    elif isinstance(t, str):
        f.write('%s%s = str\n\n' % (baseIndent, name))
        return True
    elif inspect.isclass(t):
        if noclasses: return
        try:
            f.write('%sclass %s:\n%s    def __init__(self):\n%s        pass\n' % (baseIndent, name, baseIndent, baseIndent))
        except:
            f.write('%sclass %s:\n%s    def __init__(self):\n%s        pass\n' % (baseIndent, t.__name__, baseIndent, baseIndent))

        for _name in dir(t):
            if _name in skip:
                continue
            try:
                _t = eval('%s.%s' %(name, _name))
            except:
                return False
            record(_t, _name, f, noclasses=True, baseIndent=('%s    ' % baseIndent))

        return True

    elif callable(t):
        if hasattr(t, '__objclass__'):
            f.write('%sdef %s(self):\n%s    pass\n' % (baseIndent, t.__name__, baseIndent))
        else:
            f.write('%sdef %s():\n%s    pass\n' % (baseIndent, t.__name__, baseIndent))
            return True
    return False

def generateCore(base_name, modules):

    f = open('predef/panda3d.%s.pypredef' % base_name, 'w+')

    for module in modules:
        for name in dir(module):
            try:
                exec(importptrn % (base_name, name))
                t = eval(name)

                print "Building %s..." % name
                record(t, name, f)

            except Exception, e:
                print e
                continue

    f.close()

if __name__ == '__main__':
    for (name, module) in BUILD.items():
        generateCore(name, module)