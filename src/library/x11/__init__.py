
import ctypes as ct
from src.library.x11.x11types import *

from src.engine.utils.bindinghelper import define_function


libx11 = "X11"

NoEventMask = 0
KeyPressMask = 1<<0
KeyReleaseMask = 1<<1
ButtonPressMask = 1<<2
ButtonReleaseMask = 1<<3
EnterWindowMask = 1<<4
LeaveWindowMask = 1<<5
PointerMotionMask = 1<<6
PointerMotionHintMask = 1<<7
Button1MotionMask = 1<<8
Button2MotionMask = 1<<9
Button3MotionMask = 1<<10
Button4MotionMask = 1<<11
Button5MotionMask = 1<<12
ButtonMotionMask = 1<<13
KeymapStateMask = 1<<14
ExposureMask = 1<<15
VisibilityChangeMask = 1<<16
StructureNotifyMask = 1<<17
ResizeRedirectMask = 1<<18
SubstructureNotifyMask = 1<<19
SubstructureRedirectMask = 1<<20
FocusChangeMask = 1<<21
PropertyChangeMask = 1<<22
ColormapChangeMask = 1<<23
OwnerGrabButtonMask = 1<<24

KeyPress = 2
KeyRelease = 3
ButtonPress = 4
ButtonRelease = 5
MotionNotify = 6
EnterNotify = 7
LeaveNotify = 8
FocusIn = 9
FocusOut = 10
KeymapNotify = 11
Expose = 12
GraphicsExpose = 13
NoExpose = 14
VisibilityNotify = 15
CreateNotify = 16
DestroyNotify = 17
UnmapNotify = 18
MapNotify = 19
MapRequest = 20
ReparentNotify = 21
ConfigureNotify = 22
ConfigureRequest = 23
GravityNotify = 24
ResizeRequest = 25
CirculateNotify = 26
CirculateRequest = 27
PropertyNotify = 28
SelectionClear = 29
SelectionRequest = 30
SelectionNotify = 31
ColormapNotify = 32
ClientMessage = 33
MappingNotify = 34
GenericEvent = 35
LASTEvent = 36


XOpenDisplay = define_function(libx11, 'XOpenDisplay', ct.POINTER(Display), (ct.c_char_p,))

_xCreateSimpleWindowParams = (ct.POINTER(Display), Window, ct.c_int, ct.c_int, ct.c_uint,
                              ct.c_uint, ct.c_uint, ct.c_ulong, ct.c_ulong)
XCreateSimpleWindow = define_function(libx11, 'XCreateSimpleWindow', Window, _xCreateSimpleWindowParams)

XSelectInput = define_function(libx11, 'XSelectInput', ct.c_int, (ct.POINTER(Display), Window, ct.c_long))

XMapWindow = define_function(libx11, 'XMapWindow', ct.c_int, (ct.POINTER(Display), Window))

XSelectInput = define_function(libx11, 'XSelectInput', ct.c_int, (ct.POINTER(Display), Window, ct.c_long))

XCreateGC = define_function(libx11, 'XCreateGC', GC, (ct.POINTER(Display), Drawable, ct.c_ulong, ct.POINTER(XGCValues)) )

XDefaultScreen = define_function(libx11, 'XDefaultScreen', ct.c_int, (ct.POINTER(Display),))

XDefaultRootWindow = define_function(libx11, 'XDefaultRootWindow', Window, (ct.POINTER(Display),))

XBlackPixel = define_function(libx11, 'XBlackPixel', ct.c_ulong, (ct.POINTER(Display), ct.c_int))

XFlush = define_function(libx11, 'XFlush', None, (ct.POINTER(Display),))

XNextEvent = define_function(libx11, 'XNextEvent', ct.c_int, (ct.POINTER(Display), ct.POINTER(XEvent)))

XPending = define_function(libx11, 'XPending', ct.c_int, (ct.POINTER(Display),))

XStoreName = define_function(libx11, 'XStoreName', ct.c_int, (ct.POINTER(Display), Window, ct.c_char_p) )

XInternAtom = define_function(libx11, 'XInternAtom', Atom, (ct.POINTER(Display), ct.c_char_p, Bool))

XSetWMProtocols = define_function(libx11, 'XSetWMProtocols', Status, (ct.POINTER(Display), Window, ct.POINTER(Atom)))
#define_function(libX11, )
