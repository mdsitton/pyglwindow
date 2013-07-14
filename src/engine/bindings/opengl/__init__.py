
from src.engine.window import Window
from src.engine.bindings.opengl.gl import *
from src.engine.bindings.opengl.wgl import *
tempcontext = Window(0, 0, 2, '0', 2.1)
from src.engine.bindings.opengl.wglext import *
from src.engine.bindings.opengl.glext import *
del tempcontext
del Window