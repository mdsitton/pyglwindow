# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from src.engine.bindings.opengl import *
from src.engine.window import WinMain
from src.engine.utils.file import get_path
import sys

class Main(object):

    def __init__(self, width=800, height=600, fullscreen=False):
       
        self.window = WinMain()
        
        self.width = width
        self.height = height
        
        self.fullscreen = fullscreen
        
        self.title = "Hello World!"
        
        self.path = get_path()
        
        self.window.register_init(self.init)
        self.window.register_update(self.update)
        self.window.register_render(self.render)
        self.window.register_resize(self.resize)
        # self.window.register_destroy(self.exit)
        
        self.window.create(self.width, self.height, self.fullscreen, self.title)
        
        
    def init(self):
        glVersionMajor = c_int(-1)
        glVersionMinor = c_int(-1)
        glGetIntegerv(GL_MAJOR_VERSION, pointer(glVersionMajor))
        glGetIntegerv(GL_MINOR_VERSION, pointer(glVersionMinor))
        
        print "OpenGL Version: %d.%d"% (glVersionMinor.value, glVersionMajor.value)
    
    def update(self):
        pass

    def resize(self, width, height):
        glViewport(0, 0, width, height)
        glClearColor(0.0, 0.0, 0.0, 1.0)
    
    def render(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClear(GL_COLOR_BUFFER_BIT)
        self.window.flip()
        
    def exit(self):
        # Cleanup stuff goes here
        pass

if __name__ == "__main__":
    Main()
        
