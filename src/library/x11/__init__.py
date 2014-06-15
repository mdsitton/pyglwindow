
import ctypes as ct

from src.engine.utils.bindinghelper import define_function


libx11 = "X11"

Bool = ct.c_int
Status = ct.c_int
Atom = ct.c_ulong
Time = ct.c_ulong
XID = ct.c_ulong
XPointer = ct.c_char_p
VisualID = ct.c_ulong
GContext = XID
Colormap = XID
Drawable = XID
Pixmap = XID
Font = XID
Window = XID

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

# typedef struct _XExtData {
#     int number;                   # number returned by XRegisterExtension
#     struct _XExtData *next;       # next item on list of data for structure
#     int (*free_private)(          # called to free private storage
#     struct _XExtData *extension
#     );
#     XPointer private_data;        # data private to this extension.
# } XExtData;

class _XExtData(ct.Structure):pass

_XExtData._fields_= [('number', ct.c_int),
                     ('next', ct.POINTER(_XExtData)),
                     ('free_private', ct.POINTER(ct.CFUNCTYPE(ct.c_int, ct.POINTER(_XExtData)))),
                     ('private_data', XPointer)]
XExtData = _XExtData

# typedef struct {
#     XExtData *ext_data; /* hook for extension to hang data */
#     int depth;      /* depth of this image format */
#     int bits_per_pixel; /* bits/pixel at this depth */
#     int scanline_pad;   /* scanline must padded to this multiple */
# } ScreenFormat;

class ScreenFormat(ct.Structure):
    _fields_ = [('ext_data', ct.POINTER(XExtData)),
                ('depth', ct.c_int),
                ('bits_per_pixel', ct.c_int),
                ('scanline_pad', ct.c_int)]

# typedef struct {
#     XExtData *ext_data; /* hook for extension to hang data */
#     VisualID visualid;  /* visual id of this visual */
#     int class;      /* class of screen (monochrome, etc.) */
#     unsigned long red_mask, green_mask, blue_mask;  /* mask values */
#     int bits_per_rgb;   /* log base 2 of distinct color values */
#     int map_entries;    /* color map entries */
# } Visual;

class Visual(ct.Structure):
    _fields_ = [('ext_data', ct.POINTER(XExtData)),
                ('visualid', VisualID),
                ('class', ct.c_int),
                ('red_mask', ct.c_ulong),
                ('bits_per_rgb', ct.c_int),
                ('map_entries', ct.c_int)]

# typedef struct {
#     int depth;      /* this depth (Z) of the depth */
#     int nvisuals;       /* number of Visual types at this depth */
#     Visual *visuals;    /* list of visuals possible at this depth */
# } Depth;

class Depth(ct.Structure):
    _fields_ = [('depth', ct.c_int),
                ('nvisuals', ct.c_int),
                ('visuals', ct.POINTER(Visual))]

# typedef struct _XGC
# #ifdef XLIB_ILLEGAL_ACCESS
# {
#     XExtData *ext_data; /* hook for extension to hang data */
#     GContext gid;   /* protocol ID for graphics context */
#     /* there is more to this structure, but it is private to Xlib */
# }
# #endif
# *GC;

class _XGC(ct.Structure):
    _fields_ = [('ext_data', ct.POINTER(XExtData)),
                ('gid', GContext)]
GC = ct.POINTER(_XGC)

# struct _XDisplay;       /* Forward declare before use for C++ */

# typedef struct {
#     XExtData *ext_data; /* hook for extension to hang data */
#     struct _XDisplay *display;/* back pointer to display structure */
#     Window root;        /* Root window id. */
#     int width, height;  /* width and height of screen */
#     int mwidth, mheight;    /* width and height of  in millimeters */
#     int ndepths;        /* number of depths possible */
#     Depth *depths;      /* list of allowable depths on the screen */
#     int root_depth;     /* bits per pixel */
#     Visual *root_visual;    /* root visual */
#     GC default_gc;      /* GC for the root root visual */
#     Colormap cmap;      /* default color map */
#     unsigned long white_pixel;
#     unsigned long black_pixel;  /* White and Black pixel values */
#     int max_maps, min_maps; /* max and min color maps */
#     int backing_store;  /* Never, WhenMapped, Always */
#     Bool save_unders;
#     long root_input_mask;   /* initial root input mask */
# } Screen;

class _XDisplay(ct.Structure): pass

class Screen(ct.Structure):
    _fields_ = [('ext_data', ct.POINTER(XExtData)),
                ('display', ct.POINTER(_XDisplay)),
                ('root', Window),
                ('width', ct.c_int),
                ('height', ct.c_int),
                ('mwidth', ct.c_int),
                ('mheight', ct.c_int),
                ('ndepths', ct.c_int),
                ('depths', ct.POINTER(Depth)),
                ('root_depth', ct.c_int),
                ('root_visual', ct.POINTER(Visual)),
                ('default_gc', GC),
                ('cmap', Colormap),
                ('white_pixel', ct.c_ulong),
                ('black_pixel', ct.c_ulong),
                ('max_maps', ct.c_int),
                ('min_maps', ct.c_int),
                ('backing_store', ct.c_int),
                ('save_unders', Bool),
                ('root_input_mask', ct.c_long)]


# typedef struct _XDisplay
# {
#   XExtData *ext_data;                             # hook for extension to hang data
#   struct _XPrivate *private1;
#   int fd;                                     # Network socket.
#   int private2;
#   int proto_major_version;                        # major version of server's X protocol
#   int proto_minor_version;                        # minor version of servers X protocol
#   char *vendor;                               # vendor of the server hardware
#         XID private3;
#   XID private4;
#   XID private5;
#   int private6;
#   XID (*resource_alloc)(                          # allocator function
#     struct _XDisplay*
#   );
#   int byte_order;                               # screen byte order, LSBFirst, MSBFirst
#   int bitmap_unit;                              # padding and data requirements
#   int bitmap_pad;                               # padding requirements on bitmaps
#   int bitmap_bit_order;                         # LeastSignificant or MostSignificant
#   int nformats;                               # number of pixmap formats in list
#   ScreenFormat *pixmap_format;                    # pixmap format list
#   int private8;
#   int release;                                # release of the server
#   struct _XPrivate *private9, *private10;
#   int qlen;                                   # Length of input event queue
#   unsigned long last_request_read;                # seq number of last event read
#   unsigned long request;                          # sequence number of last request.
#   XPointer private11;
#   XPointer private12;
#   XPointer private13;
#   XPointer private14;
#   unsigned max_request_size;                      # maximum number 32 bit words in request
#   struct _XrmHashBucketRec *db;
#   int (*private15)(
#     struct _XDisplay*
#     );
#   char *display_name;                             # "host:display" string used on this connect
#   int default_screen;                             # default screen for operations
#   int nscreens;                               # number of screens on this server
#   Screen *screens;                              # pointer to list of screens
#   unsigned long motion_buffer;                  # size of motion buffer
#   unsigned long private16;
#   int min_keycode;                              # minimum defined keycode
#   int max_keycode;                              # maximum defined keycode
#   XPointer private17;
#   XPointer private18;
#   int private19;
#   char *xdefaults;                              # contents of defaults from server
#                                                   # there is more to this structure, but it is private to Xlib
# } Display, *_XPrivDisplay;
class _XPrivate(ct.Structure):
    pass

_XDisplay._fields_ = [('ext_data', ct.POINTER(XExtData)),
                      ('private1', ct.POINTER(_XPrivate)),
                      ('fd', ct.c_int),
                      ('private2', ct.c_int),
                      ('proto_minor_version', ct.c_int),
                      ('proto_minor_version', ct.c_int),
                      ('vendor', ct.c_char_p),
                      ('private3', XID),
                      ('private4', XID),
                      ('private5', XID),
                      ('private6', ct.c_int),
                      ('resource_alloc', ct.POINTER(ct.CFUNCTYPE(XID, ct.POINTER(_XDisplay)))),
                      ('byte_order', ct.c_int),
                      ('bitmap_unit', ct.c_int),
                      ('bitmap_pad', ct.c_int),
                      ('bitmap_bit_order', ct.c_int),
                      ('nformats', ct.c_int),
                      ('pixmap_format', ScreenFormat),
                      ('private8', ct.c_int),
                      ('release', ct.c_int),
                      ('private9', ct.POINTER(_XPrivate)),
                      ('private10', ct.POINTER(_XPrivate)),
                      ('qlen', ct.c_int),
                      ('last_request_read', ct.c_ulong),
                      ('request', ct.c_ulong),
                      ('private11', XPointer),
                      ('private12', XPointer),
                      ('private13', XPointer),
                      ('private14', XPointer),
                      ('max_request_size', ct.c_uint),
                      ('private15', ct.CFUNCTYPE(ct.c_int, ct.POINTER(_XDisplay))),
                      ('display_name', ct.c_char_p),
                      ('default_screen', ct.c_int),
                      ('nscreens', ct.c_int),
                      ('screens', ct.POINTER(Screen)),
                      ('motion_buffer', ct.c_ulong),
                      ('private16', ct.c_ulong),
                      ('min_keycode', ct.c_int),
                      ('max_keycode', ct.c_int),
                      ('private17', XPointer),
                      ('private18', XPointer),
                      ('private19', ct.c_int),
                      ('xdefaults', ct.c_char_p)]
Display = _XDisplay

# typedef struct {
#     int function;       /* logical operation */
#     unsigned long plane_mask;/* plane mask */
#     unsigned long foreground;/* foreground pixel */
#     unsigned long background;/* background pixel */
#     int line_width;     /* line width */
#     int line_style;     /* LineSolid, LineOnOffDash, LineDoubleDash */
#     int cap_style;      /* CapNotLast, CapButt,
#                    CapRound, CapProjecting */
#     int join_style;     /* JoinMiter, JoinRound, JoinBevel */
#     int fill_style;     /* FillSolid, FillTiled,
#                    FillStippled, FillOpaeueStippled */
#     int fill_rule;      /* EvenOddRule, WindingRule */
#     int arc_mode;       /* ArcChord, ArcPieSlice */
#     Pixmap tile;        /* tile pixmap for tiling operations */
#     Pixmap stipple;     /* stipple 1 plane pixmap for stipping */
#     int ts_x_origin;    /* offset for tile or stipple operations */
#     int ts_y_origin;
#         Font font;          /* default text font for text operations */
#     int subwindow_mode;     /* ClipByChildren, IncludeInferiors */
#     Bool graphics_exposures;/* boolean, should exposures be generated */
#     int clip_x_origin;  /* origin for clipping */
#     int clip_y_origin;
#     Pixmap clip_mask;   /* bitmap clipping; other calls for rects */
#     int dash_offset;    /* patterned/dashed line information */
#     char dashes;
# } XGCValues;

class XGCValues(ct.Structure):
    _fields_ = [('function', ct.c_int),
                ('plane_mask', ct.c_ulong),
                ('foreground', ct.c_ulong),
                ('background', ct.c_ulong),
                ('line_width', ct.c_int),
                ('line_style', ct.c_int),
                ('cap_style', ct.c_int),
                ('join_style', ct.c_int),
                ('fill_style', ct.c_int),
                ('fill_rule', ct.c_int),
                ('arc_mode', ct.c_int),
                ('tile', Pixmap),
                ('stipple', Pixmap),
                ('ts_x_origin', ct.c_int),
                ('ts_y_origin', ct.c_int),
                ('font', Font),
                ('subwindow_mode', ct.c_int),
                ('graphics_exposures', Bool),
                ('clip_x_origin', ct.c_int),
                ('clip_y_origin', ct.c_int),
                ('clip_mask', Pixmap),
                ('dash_offset', ct.c_int),
                ('dashes', ct.c_char)]

# typedef struct {
#     int type;       /* of event */
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;          /* "event" window it is reported relative to */
#     Window root;            /* root window that the event occurred on */
#     Window subwindow;   /* child window */
#     Time time;      /* milliseconds */
#     int x, y;       /* pointer x, y coordinates in event window */
#     int x_root, y_root; /* coordinates relative to root */
#     unsigned int state; /* key or button mask */
#     unsigned int keycode;   /* detail */
#     Bool same_screen;   /* same screen flag */
# } XKeyEvent;
# typedef XKeyEvent XKeyPressedEvent;
# typedef XKeyEvent XKeyReleasedEvent;

class XKeyEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('root', Window),
                ('subwindow', Window),
                ('time', Time),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('x_root', ct.c_int),
                ('y_root', ct.c_int),
                ('state', ct.c_uint),
                ('keycode', ct.c_uint),
                ('same_screen', Bool)]

XKeyPressedEvent = XKeyEvent
XKeyReleasedEvent = XKeyEvent

# typedef struct {
#     int type;       /* of event */
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;          /* "event" window it is reported relative to */
#     Window root;            /* root window that the event occurred on */
#     Window subwindow;   /* child window */
#     Time time;      /* milliseconds */
#     int x, y;       /* pointer x, y coordinates in event window */
#     int x_root, y_root; /* coordinates relative to root */
#     unsigned int state; /* key or button mask */
#     unsigned int button;    /* detail */
#     Bool same_screen;   /* same screen flag */
# } XButtonEvent;
# typedef XButtonEvent XButtonPressedEvent;
# typedef XButtonEvent XButtonReleasedEvent;
class XButtonEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('root', Window),
                ('subwindow', Window),
                ('time', Time),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('x_root', ct.c_int),
                ('y_root', ct.c_int),
                ('state', ct.c_uint),
                ('button', ct.c_uint),
                ('same_screen', Bool)]

XButtonPressedEvent = XButtonEvent
XButtonReleasedEvent = XButtonEvent
# typedef struct {
#     int type;       /* of event */
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;          /* "event" window reported relative to */
#     Window root;            /* root window that the event occurred on */
#     Window subwindow;   /* child window */
#     Time time;      /* milliseconds */
#     int x, y;       /* pointer x, y coordinates in event window */
#     int x_root, y_root; /* coordinates relative to root */
#     unsigned int state; /* key or button mask */
#     char is_hint;       /* detail */
#     Bool same_screen;   /* same screen flag */
# } XMotionEvent;
# typedef XMotionEvent XPointerMovedEvent;
class XMotionEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('root', Window),
                ('subwindow', Window),
                ('time', Time),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('x_root', ct.c_int),
                ('y_root', ct.c_int),
                ('state', ct.c_uint),
                ('is_hint', ct.c_char),
                ('same_screen', Bool)]

XPointerMovedEvent = XMotionEvent

# typedef struct {
#     int type;       /* of event */
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;          /* "event" window reported relative to */
#     Window root;            /* root window that the event occurred on */
#     Window subwindow;   /* child window */
#     Time time;      /* milliseconds */
#     int x, y;       /* pointer x, y coordinates in event window */
#     int x_root, y_root; /* coordinates relative to root */
#     int mode;       /* NotifyNormal, NotifyGrab, NotifyUngrab */
#     int detail;
#     /*
#      * NotifyAncestor, NotifyVirtual, NotifyInferior,
#      * NotifyNonlinear,NotifyNonlinearVirtual
#      */
#     Bool same_screen;   /* same screen flag */
#     Bool focus;     /* boolean focus */
#     unsigned int state; /* key or button mask */
# } XCrossingEvent;
# typedef XCrossingEvent XEnterWindowEvent;
# typedef XCrossingEvent XLeaveWindowEvent;

class XCrossingEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('root', Window),
                ('subwindow', Window),
                ('time', Time),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('x_root', ct.c_int),
                ('y_root', ct.c_int),
                ('mode', ct.c_int),
                ('detail', ct.c_int),
                ('same_screen', Bool),
                ('focus', Bool),
                ('state', ct.c_uint)]
XEnterWindowEvent = XCrossingEvent
XLeaveWindowEvent = XCrossingEvent

# typedef struct {
#     int type;       /* FocusIn or FocusOut */
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;      /* window of event */
#     int mode;       /* NotifyNormal, NotifyWhileGrabbed,
#                    NotifyGrab, NotifyUngrab */
#     int detail;
#     /*
#      * NotifyAncestor, NotifyVirtual, NotifyInferior,
#      * NotifyNonlinear,NotifyNonlinearVirtual, NotifyPointer,
#      * NotifyPointerRoot, NotifyDetailNone
#      */
# } XFocusChangeEvent;
# typedef XFocusChangeEvent XFocusInEvent;
# typedef XFocusChangeEvent XFocusOutEvent;

class XFocusChangeEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('mode', ct.c_int),
                ('detail', ct.c_int),]
XFocusInEvent = XFocusChangeEvent
XFocusOutEvent = XFocusChangeEvent

# /* generated on EnterWindow and FocusIn  when KeyMapState selected */
# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     char key_vector[32];
# } XKeymapEvent;

class XKeymapEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('key_vector', (ct.c_char*32))]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     int x, y;
#     int width, height;
#     int count;      /* if non-zero, at least this many more */
# } XExposeEvent;

class XExposeEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('width', ct.c_int),
                ('height', ct.c_int),
                ('count', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Drawable drawable;
#     int x, y;
#     int width, height;
#     int count;      /* if non-zero, at least this many more */
#     int major_code;     /* core is CopyArea or CopyPlane */
#     int minor_code;     /* not defined in the core */
# } XGraphicsExposeEvent;

class XGraphicsExposeEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('drawable', Drawable),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('width', ct.c_int),
                ('height', ct.c_int),
                ('count', ct.c_int),
                ('major_code', ct.c_int),
                ('minor_code', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Drawable drawable;
#     int major_code;     /* core is CopyArea or CopyPlane */
#     int minor_code;     /* not defined in the core */
# } XNoExposeEvent;

class XNoExposeEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('drawable', Drawable),
                ('major_code', ct.c_int),
                ('minor_code', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     int state;      /* Visibility state */
# } XVisibilityEvent;

class XVisibilityEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('state', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window parent;      /* parent of the window */
#     Window window;      /* window id of window created */
#     int x, y;       /* window location */
#     int width, height;  /* size of window */
#     int border_width;   /* border width */
#     Bool override_redirect; /* creation should be overridden */
# } XCreateWindowEvent;

class XCreateWindowEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('parent', Window),
                ('window', Window),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('width', ct.c_int),
                ('height', ct.c_int),
                ('border_width', ct.c_int),
                ('override_redirect', Bool)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
# } XDestroyWindowEvent;

class XDestroyWindowEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
#     Bool from_configure;
# } XUnmapEvent;

class XUnmapEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window),
                ('from_configure', Bool)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
#     Bool override_redirect; /* boolean, is override set... */
# } XMapEvent;

class XMapEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window),
                ('override_redirect', Bool)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window parent;
#     Window window;
# } XMapRequestEvent;

class XMapRequestEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('parent', Window),
                ('window', Window)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
#     Window parent;
#     int x, y;
#     Bool override_redirect;
# } XReparentEvent;

class XReparentEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window),
                ('parent', Window),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('override_redirect', Bool)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
#     int x, y;
#     int width, height;
#     int border_width;
#     Window above;
#     Bool override_redirect;
# } XConfigureEvent;

class XConfigureEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('width', ct.c_int),
                ('height', ct.c_int),
                ('border_width', ct.c_int),
                ('above', Window),
                ('override_redirect', Bool)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
#     int x, y;
# } XGravityEvent;

class XGravityEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window),
                ('x', ct.c_int),
                ('y', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     int width, height;
# } XResizeRequestEvent;

class XResizeRequestEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('width', ct.c_int),
                ('height', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window parent;
#     Window window;
#     int x, y;
#     int width, height;
#     int border_width;
#     Window above;
#     int detail;     /* Above, Below, TopIf, BottomIf, Opposite */
#     unsigned long value_mask;
# } XConfigureRequestEvent;

class XConfigureRequestEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('parent', Window),
                ('window', Window),
                ('x', ct.c_int),
                ('y', ct.c_int),
                ('width', ct.c_int),
                ('height', ct.c_int),
                ('border_width', ct.c_int),
                ('above', Window),
                ('detail', ct.c_int),
                ('value_mask', ct.c_long)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window event;
#     Window window;
#     int place;      /* PlaceOnTop, PlaceOnBottom */
# } XCirculateEvent;

class XCirculateEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('event', Window),
                ('window', Window),
                ('place', ct.c_int)]
# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window parent;
#     Window window;
#     int place;      /* PlaceOnTop, PlaceOnBottom */
# } XCirculateRequestEvent;

class XCirculateRequestEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('parent', Window),
                ('window', Window),
                ('place', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     Atom atom;
#     Time time;
#     int state;      /* NewValue, Deleted */
# } XPropertyEvent;

class XPropertyEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('atom', Atom),
                ('time', Time),
                ('state', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     Atom selection;
#     Time time;
# } XSelectionClearEvent;

class XSelectionClearEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('selection', Atom),
                ('time', Time)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window owner;
#     Window requestor;
#     Atom selection;
#     Atom target;
#     Atom property;
#     Time time;
# } XSelectionRequestEvent;

class XSelectionRequestEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('owner', Window),
                ('requestor', Window),
                ('selection', Atom),
                ('target', Atom),
                ('property', Atom),
                ('time', Time)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window requestor;
#     Atom selection;
#     Atom target;
#     Atom property;      /* ATOM or None */
#     Time time;
# } XSelectionEvent;

class XSelectionEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('requestor', Window),
                ('selection', Atom),
                ('target', Atom),
                ('property', Atom),
                ('time', Time)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     Colormap colormap;  /* COLORMAP or None */
#     Bool new;
#     int state;      /* ColormapInstalled, ColormapUninstalled */
# } XColormapEvent;

class XColormapEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('colormap', Colormap),
                ('new', Bool),
                ('state', ct.c_int)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;
#     Atom message_type;
#     int format;
#     union {
#         char b[20];
#         short s[10];
#         long l[5];
#         } data;
# } XClientMessageEvent;
class _XClientMessageEvent_u(ct.Union):
    _fields_ = [('b', (ct.c_char*20)),
                ('s', (ct.c_short*10)),
                ('l', (ct.c_long*5))]
class XClientMessageEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('message_type', Atom),
                ('format', ct.c_int),
                ('data', _XClientMessageEvent_u)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;   /* Display the event was read from */
#     Window window;      /* unused */
#     int request;        /* one of MappingModifier, MappingKeyboard,
#                    MappingPointer */
#     int first_keycode;  /* first keycode */
#     int count;      /* defines range of change w. first_keycode*/
# } XMappingEvent;

class XMappingEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window),
                ('request', ct.c_int),
                ('first_keycode', ct.c_int),
                ('count', ct.c_int)]

# typedef struct {
#     int type;
#     Display *display;   /* Display the event was read from */
#     XID resourceid;     /* resource id */
#     unsigned long serial;   /* serial number of failed request */
#     unsigned char error_code;   /* error code of failed request */
#     unsigned char request_code; /* Major op-code of failed request */
#     unsigned char minor_code;   /* Minor op-code of failed request */
# } XErrorEvent;

class XErrorEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('display', ct.POINTER(Display)),
                ('resourceid', XID),
                ('serial', ct.c_ulong),
                ('error_code', ct.c_ubyte),
                ('request_code', ct.c_ubyte),
                ('minor_code', ct.c_ubyte)]

# typedef struct {
#     int type;
#     unsigned long serial;   /* # of last request processed by server */
#     Bool send_event;    /* true if this came from a SendEvent request */
#     Display *display;/* Display the event was read from */
#     Window window;  /* window on which event was requested in event mask */
# } XAnyEvent;

class XAnyEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('window', Window)]


# typedef struct
#     {
#     int            type;         /* of event. Always GenericEvent */
#     unsigned long  serial;       /* # of last request processed */
#     Bool           send_event;   /* true if from SendEvent request */
#     Display        *display;     /* Display the event was read from */
#     int            extension;    /* major opcode of extension that caused the event */
#     int            evtype;       /* actual event type. */
#     } XGenericEvent;

class XGenericEvent(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('extension', ct.c_int),
                ('evtype', ct.c_int)]

# typedef struct {
#     int            type;         /* of event. Always GenericEvent */
#     unsigned long  serial;       /* # of last request processed */
#     Bool           send_event;   /* true if from SendEvent request */
#     Display        *display;     /* Display the event was read from */
#     int            extension;    /* major opcode of extension that caused the event */
#     int            evtype;       /* actual event type. */
#     unsigned int   cookie;
#     void           *data;
# } XGenericEventCookie;

class XGenericEventCookie(ct.Structure):
    _fields_ = [('type', ct.c_int),
                ('serial', ct.c_ulong),
                ('send_event', Bool),
                ('display', ct.POINTER(Display)),
                ('extension', ct.c_int),
                ('evtype', ct.c_int),
                ('cookie', ct.c_uint),
                ('data', ct.c_void_p)]

# typedef union _XEvent {
#         int type;       /* must not be changed; first element */
#     XAnyEvent xany;
#     XKeyEvent xkey;
#     XButtonEvent xbutton;
#     XMotionEvent xmotion;
#     XCrossingEvent xcrossing;
#     XFocusChangeEvent xfocus;
#     XExposeEvent xexpose;
#     XGraphicsExposeEvent xgraphicsexpose;
#     XNoExposeEvent xnoexpose;
#     XVisibilityEvent xvisibility;
#     XCreateWindowEvent xcreatewindow;
#     XDestroyWindowEvent xdestroywindow;
#     XUnmapEvent xunmap;
#     XMapEvent xmap;
#     XMapRequestEvent xmaprequest;
#     XReparentEvent xreparent;
#     XConfigureEvent xconfigure;
#     XGravityEvent xgravity;
#     XResizeRequestEvent xresizerequest;
#     XConfigureRequestEvent xconfigurerequest;
#     XCirculateEvent xcirculate;
#     XCirculateRequestEvent xcirculaterequest;
#     XPropertyEvent xproperty;
#     XSelectionClearEvent xselectionclear;
#     XSelectionRequestEvent xselectionrequest;
#     XSelectionEvent xselection;
#     XColormapEvent xcolormap;
#     XClientMessageEvent xclient;
#     XMappingEvent xmapping;
#     XErrorEvent xerror;
#     XKeymapEvent xkeymap;
#     XGenericEvent xgeneric;
#     XGenericEventCookie xcookie;
#     long pad[24];
# } XEvent;

class _XEvent(ct.Union):
    _fields_ = [('type', ct.c_int),
                ('xany', XAnyEvent),
                ('xkey', XKeyEvent),
                ('xbutton', XButtonEvent),
                ('xmotion', XMotionEvent),
                ('xcrossing', XCrossingEvent),
                ('xfocus', XFocusChangeEvent),
                ('xexpose', XExposeEvent),
                ('xgraphicsexpose', XGraphicsExposeEvent),
                ('xnoexpose', XNoExposeEvent),
                ('xvisibility', XVisibilityEvent),
                ('xcreatewindow', XCreateWindowEvent),
                ('xdestroywindow', XDestroyWindowEvent),
                ('xunmap', XUnmapEvent),
                ('xmap', XMapEvent),
                ('xmaprequest', XMapRequestEvent),
                ('xreparent', XReparentEvent),
                ('xconfigure', XConfigureEvent),
                ('xgravity', XGravityEvent),
                ('xresizerequest', XResizeRequestEvent),
                ('xconfigurerequest', XConfigureRequestEvent),
                ('xcirculate', XCirculateEvent),
                ('xcirculaterequest', XCirculateRequestEvent),
                ('xproperty', XPropertyEvent),
                ('xselectionclear', XSelectionClearEvent),
                ('xselectionrequest', XSelectionRequestEvent),
                ('xselection', XSelectionEvent),
                ('xcolormap', XColormapEvent),
                ('xclient', XClientMessageEvent),
                ('xmapping', XMappingEvent),
                ('xerror', XErrorEvent),
                ('xkeymap', XKeymapEvent),
                ('xgeneric', XGenericEvent),
                ('xcookie', XGenericEventCookie),
                ('pad', ct.c_long*24)]
XEvent = _XEvent

Display = XDisplay = _XDisplay
_XPrivDisplay = ct.POINTER(_XDisplay)


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
