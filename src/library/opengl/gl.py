from src.engine.utils.bindinghelper import define_function
from src.library.opengl.gltypes import *


# Dll Names
opengl32 = "opengl32"
glu32 = "glu32"

# Cull Face
GL_FRONT_LEFT = 0x0400
GL_FRONT_RIGHT = 0x0401
GL_BACK_LEFT = 0x0402
GL_BACK_RIGHT = 0x0403
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_LEFT = 0x0406
GL_RIGHT = 0x0407
GL_FRONT_AND_BACK = 0x0408

GL_NONE = 0
GL_POINTS = 0x0000

# Face winding
GL_CW = 0x0900
GL_CCW = 0x0901

# OLD OpenGL macros
GLEW_OK = 0
GLEW_VERSION = 1

GL_COLOR_BUFFER_BIT = 0x00004000
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
GL_STENCIL_BUFFER_BIT = 0x00000400

GL_DEPTH_COMPONENT = 0x1902

GL_PROJECTION = 0x1701
GL_MODELVIEW = 0x1700
GL_QUADS = 0x0007
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_POLYGON = 0x0009
GL_VERTEX_ARRAY = 0x8074
GL_NORMAL_ARRAY = 0x8075

GL_POSITION = 0x1203

GL_LIGHT0 = 0x4000

GL_DEPTH_TEST = 0x0B71

GL_COMPILE = 0x1300

# Types
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405

GL_FLOAT = 0x1406
GL_DOUBLE = 0x140A

GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401

GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403

# BOOLEANS
GL_TRUE = 1
GL_FALSE = 0

GL_FLAT = 0x1D00
GL_SMOOTH = 0x1D01

GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207

GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50

GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102

GL_BLEND = 0x0BE2

GL_SRC_COLOR = 0x0300
GL_SRC_ALPHA = 0x0302
GL_DST_ALPHA = 0x0304
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308

# Polygon stuff
GL_POLYGON_MODE = 0x0B40
GL_POLYGON_SMOOTH = 0x0B41
GL_POLYGON_STIPPLE = 0x0B42

GL_CULL_FACE = 0x0B44

# OpenGL ARB macros
GL_VERTEX_SHADER_ARB = 0x8B31
GL_FRAGMENT_SHADER_ARB = 0x8B30

GL_MAJOR_VERSION = 0x821B
GL_MINOR_VERSION = 0x821C

GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_BUFFER_SIZE_ARB = 0x8764
GL_BUFFER_SIZE = 0x8764

GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31

GL_STATIC_DRAW = 0x88E4
GL_STREAM_DRAW = 0x88E0

GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_INFO_LOG_LENGTH = 0x8B84

# Textures Version GL 1.3
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF

GL_TEXTURE_1D = 0x0DE0
GL_TEXTURE_2D = 0x0DE1

GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_CLAMP = 0x2900
GL_REPEAT = 0x2901

GL_CLAMP_TO_EDGE = 0x812F

GL_DEPTH_TEXTURE_MODE = 0x884B
GL_TEXTURE_COMPARE_MODE = 0x884C
GL_TEXTURE_COMPARE_FUNC = 0x884D
GL_COMPARE_R_TO_TEXTURE = 0x884E

GL_LUMINANCE = 0x1909

GL_COMPARE_R_TO_TEXTURE_ARB = 0x884E
GL_COMPARE_REF_TO_TEXTURE = GL_COMPARE_R_TO_TEXTURE_ARB

# RGBA STUFF
GL_RGB = 0x1907
GL_RGBA = 0x1908

GL_RGB4 = 0x804F
GL_RGB5 = 0x8050
GL_RGB8 = 0x8051
GL_RGB10 = 0x8052
GL_RGB12 = 0x8053
GL_RGB16 = 0x8054
GL_RGBA2 = 0x8055
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGBA8 = 0x8058
GL_RGB10_A2 = 0x8059
GL_RGBA12 = 0x805A
GL_RGBA16 = 0x805B



# Used when a function has no params instead of the (), it looks cleaner.
noParams = ()


# GLU
gluLookAtParams  = (c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double)
gluLookAt = define_function( glu32, 'gluLookAt', None, gluLookAtParams )

gluPerspectiveParams = (c_double, c_double, c_double, c_double)
gluPerspective = define_function( glu32, 'gluPerspective', None, gluPerspectiveParams )

gluProjectParams = (c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double))
gluProject = define_function( glu32, 'gluProject', GLint, gluProjectParams)


# OLD OpenGL calls
glPointSize = define_function( opengl32, 'glPointSize', None, (GLfloat,))

glClearColorParams = (c_float, c_float, c_float, c_float)
glClearColor = define_function( opengl32, 'glClearColor', None, glClearColorParams )

glGetIntegerv = define_function( opengl32, 'glGetIntegerv', None, (GLenum, POINTER(GLint)) )

glGetDoublev = define_function( opengl32, 'glGetDoublev', None, (GLenum, POINTER(GLdouble)) )

glGetFloatv = define_function(opengl32, 'glGetFloatv', None, (GLenum, POINTER(GLfloat)) )

glClear = define_function( opengl32, 'glClear', None, (GLbitfield,) )

glLoadIdentity = define_function( opengl32, 'glLoadIdentity', None, noParams )

glLightfvParams = (c_uint, c_uint, POINTER(c_float))
glLightfv = define_function( opengl32, 'glLightfv', None, glLightfvParams )

glRotatefParams = (c_float, c_float, c_float, c_float)
glRotatef = define_function( opengl32, 'glRotatef', None, glRotatefParams )

glColor3fParams = (c_float, c_float, c_float)
glColor3f = define_function( opengl32, 'glColor3f', None, glColor3fParams )

glBegin = define_function( opengl32, 'glBegin', None, (GLenum,) )

glEnd = define_function( opengl32, 'glEnd', None, noParams )

glVertex3fParams = (c_float, c_float, c_float)
glVertex3f = define_function( opengl32, 'glVertex3f', None, glVertex3fParams )

glNormal3fParams = (c_float, c_float, c_float)
glNormal3f = define_function( opengl32, 'glNormal3f', None, glNormal3fParams )

glTranslatefParams  = (c_float, c_float, c_float)
glTranslatef = define_function( opengl32, 'glTranslatef', None, glTranslatefParams )

glMatrixMode = define_function( opengl32, 'glMatrixMode', None, (GLenum,) )

glViewportParams = (GLint, GLint, GLsizei, GLsizei)
glViewport = define_function( opengl32, 'glViewport', None, glViewportParams )

glEnable = define_function( opengl32, 'glEnable', None, (GLenum,) )

glDisable = define_function( opengl32, 'glDisable', None, (GLenum,))

glClearDepth = define_function( opengl32, 'glClearDepth', None, (GLclampd,) )

glCullFace = define_function(opengl32, 'glCullFace', None, (GLenum,))

glFrontFace = define_function(opengl32, 'glFrontFace', None, (GLenum,))

glDepthMask = define_function(opengl32, 'glDepthMask', None, (GLboolean,))

glDepthRange = define_function(opengl32, 'glDepthRange', None, (GLclampd, GLclampd,))

# newer ones start here
glGenLists = define_function( opengl32, 'glGenLists', GLuint, (GLsizei,) )

glNewList = define_function( opengl32, 'glNewList', None, (GLuint, GLenum) )

glPushClientAttrib = define_function( opengl32, 'glPushClientAttrib', None, (GLbitfield,) )

glEnableClientState = define_function( opengl32, 'glEnableClientState', None, (GLenum,) )

glVertexPointerParams = (GLint, GLenum, GLsizei, POINTER(GLvoid))
glVertexPointer = define_function( opengl32, 'glVertexPointer', None, glVertexPointerParams )

glNormalPointerParams = (GLenum, GLsizei, POINTER(GLvoid))
glNormalPointer = define_function( opengl32, 'glNormalPointer', None, glNormalPointerParams )

glDrawElementsParams = (GLenum, GLsizei, GLenum, POINTER(GLvoid))
glDrawElements = define_function( opengl32, 'glDrawElements', None, glDrawElementsParams )

glPopClientAttrib = define_function( opengl32, 'glPopClientAttrib', None, noParams )

glEndList = define_function( opengl32, 'glEndList', None, noParams )

glCallList = define_function( opengl32, 'glCallList', None, (GLuint,) )

glShadeModel = define_function( opengl32, 'glShadeModel', None, (GLenum,) )

glDepthFunc = define_function( opengl32, 'glDepthFunc', None, (GLenum,) )

glHint = define_function( opengl32, 'glHint', None, (GLenum, GLenum) )

glDrawArrays = define_function( opengl32, 'glDrawArrays', None, (GLenum, GLint, GLsizei) )

glGenTextures = define_function( opengl32, 'glGenTextures', None, (GLsizei, POINTER(GLuint)))

glBindTexture = define_function( opengl32, 'glBindTexture', None, (GLenum, GLuint))

glTexImage2DParams = (GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, c_void_p)
glTexImage2D = define_function( opengl32, 'glTexImage2D', None, glTexImage2DParams)

glTexParameteri = define_function (opengl32, 'glTexParameteri', None, (GLenum, GLenum, GLint))
glTexParameteriv = define_function (opengl32, 'glTexParameteriv', None, (GLenum, GLenum, POINTER(GLint)))

glTexParameterf = define_function (opengl32, 'glTexParameteri', None, (GLenum, GLenum, GLfloat))
glTexParameterfv = define_function (opengl32, 'glTexParameteriv', None, (GLenum, GLenum, POINTER(GLfloat)))

glDrawBuffer = define_function(opengl32, 'glDrawBuffer', None, (GLenum,))

glReadBuffer = define_function(opengl32, 'glReadBuffer', None, (GLenum,))

glRotated = define_function( opengl32, 'glRotated', None, (GLdouble, GLdouble, GLdouble, GLdouble))
glRotatef = define_function( opengl32, 'glRotatef', None, (GLfloat, GLfloat, GLfloat, GLfloat))

glScaled = define_function( opengl32, 'glScaled', None, (GLdouble, GLdouble, GLdouble))
glScalef = define_function( opengl32, 'glScalef', None, (GLfloat, GLfloat, GLfloat))

glBlendFunc = define_function( opengl32, 'glBlendFunc', None, (GLenum, GLenum))