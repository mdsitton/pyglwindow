from src.engine.bindings.opengl.tempcontext import Context

from src.engine.bindings.opengl.gl import *
from src.engine.bindings.opengl.wgl import *

context = Context()
from src.engine.bindings.opengl.wglext import *
from src.engine.bindings.opengl.glext import *
context.destroy()