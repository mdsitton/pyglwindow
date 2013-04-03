from src.engine.bindings.opengl.tempcontext import TempContext

from src.engine.bindings.opengl.gl import *
from src.engine.bindings.opengl.wgl import *

context = TempContext()
from src.engine.bindings.opengl.wglext import *
from src.engine.bindings.opengl.glext import *
context.delete()