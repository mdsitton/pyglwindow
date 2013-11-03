import sys
from src.engine.window import Window
from src.engine.context import Context
from src.engine.events import Events
from src.library.opengl.gl import *
from src.library.opengl.wgl import *
window = Window(0, 0, 2, '0')
events = Events()
context = Context(2.1)
window.events = events
window.context = context
from src.library.opengl.wglext import *
from src.library.opengl.glext import *
from src.library.opengl.quickgl import *
context.delete()
window.delete()