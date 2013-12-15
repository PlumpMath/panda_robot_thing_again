__author__ = 'Will'

'''
* The Great panda3d/pydev autocompletion *
*        code is in public domain        *
Created on Nov 29, 2012
@author: rndbit

1. Use generated predefines
2. Insert 'direct' and 'panda3d' to forced builtins
3. Edit pycompletionserver.py (located somewhere like in C:\Program Files\Eclipse\plugins\org.python.pydev_2.7.1.2012100913\pysrc\ )
   Insert after 'currDirModule = None':
   try:
       from pandac.PandaModules import loadPrcFileData
       loadPrcFileData("", "window-type none")
       import direct
       import direct.directbase.DirectStart
   except:
       pass
'''

import direct, __builtin__, panda3d
from panda3d import core, dtoolconfig, physics, fx, egg, ode, bullet, vision, rocket, ai #, physx, awesomium, speedtree
import direct.directbase.DirectStart
from panda3d.core import Vec2, Vec2D, Vec2F, Vec3, Vec3F, Vec3D, Vec4, Vec4F, Vec4D,\
        Point2, Point2D, Point2F, Point3, Point3D, Point3F, Point4, Point4D, Point4F,\
        VBase2, VBase2D, VBase2F, VBase3, VBase3D, VBase3F, VBase4, VBase4D, VBase4F
from direct.stdpy.file import *
from direct.stdpy import threading2 as threading

if not hasattr(__builtin__, 'base'):
    base          = None
    aspect2d      = None
    aspect2dp     = None
    bboard        = None
    bpdb          = None
    camera        = None
    config        = None
    cpMgr         = None
    deltaProfiler = None
    directNotify  = None
    direct        = None
    eventMgr      = None
    globalClock   = None
    jobMgr        = None
    loader        = None
    messenger     = None
    onScreenDebug = None
    ostream       = None
    pixel2d       = None
    pixel2dp      = None
    render        = None
    render2d      = None
    render2dp     = None
    taskMgr       = None
    vfs           = None

assert isinstance(base, direct.showbase.ShowBase.ShowBase)
assert isinstance(aspect2d, core.NodePath)
assert isinstance(aspect2dp, core.NodePath)
assert isinstance(bboard, direct.showbase.BulletinBoard.BulletinBoard)
assert isinstance(bpdb, direct.showbase.BpDb.BpDb)
assert isinstance(camera, core.NodePath)
assert isinstance(config, core.DConfig)
assert isinstance(cpMgr, core.ConfigPageManager)
assert isinstance(deltaProfiler, direct.directutil.DeltaProfiler.DeltaProfiler)
assert isinstance(directNotify, direct.directnotify.DirectNotify.DirectNotify)
assert isinstance(eventMgr, direct.showbase.EventManager.EventManager)
assert isinstance(globalClock, core.ClockObject)
assert isinstance(jobMgr, direct.showbase.JobManager.JobManager)
assert isinstance(loader, direct.showbase.Loader.Loader)
assert isinstance(messenger, direct.showbase.Messenger.Messenger)
assert isinstance(onScreenDebug, direct.showbase.OnScreenDebug.OnScreenDebug)
assert isinstance(ostream, core.ostream)
assert isinstance(pixel2d, core.NodePath)
assert isinstance(pixel2dp, core.NodePath)
assert isinstance(render, core.NodePath)
assert isinstance(render2d, core.NodePath)
assert isinstance(render2dp, core.NodePath)
assert isinstance(taskMgr, direct.task.Task.TaskManager)
assert isinstance(vfs, core.VirtualFileSystem)