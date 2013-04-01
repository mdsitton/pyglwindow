# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from src.engine.bindings.util import CreateDllFunction
from src.engine.bindings.opengl.gltypes import *


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

# Face winding
GL_CW = 0x0900
GL_CCW = 0x0901

# OLD OpenGL macros
GLEW_OK = 0
GLEW_VERSION = 1

GL_COLOR_BUFFER_BIT = 0x00004000
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002

GL_PROJECTION = 0x1701
GL_MODELVIEW = 0x1700
GL_QUADS = 0x0007
GL_TRIANGLES = 0x0004
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

GL_CULL_FACE = 0x0B44

# OpenGL ARB macros
GL_VERTEX_SHADER_ARB = 0x8B31
GL_FRAGMENT_SHADER_ARB = 0x8B30

GL_MAJOR_VERSION = 0x821B
GL_MINOR_VERSION = 0x821C

GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893

GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31

GL_STATIC_DRAW = 0x88E4

GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_INFO_LOG_LENGTH = 0x8B84


# Used when a function has no params instead of the (), it looks cleaner.
noParams = ()


# GLU
gluLookAtParams  = (c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double)
gluLookAt = CreateDllFunction( glu32, 'gluLookAt', None, gluLookAtParams )

gluPerspectiveParams = (c_double, c_double, c_double, c_double)
gluPerspective = CreateDllFunction( glu32, 'gluPerspective', None, gluPerspectiveParams )


# OLD OpenGL calls
glClearColorParams = (c_float, c_float, c_float, c_float)
glClearColor = CreateDllFunction( opengl32, 'glClearColor', None, glClearColorParams )

glGetIntegerv = CreateDllFunction( opengl32, 'glGetIntegerv', None, (GLenum, POINTER(GLint)) )

glClear = CreateDllFunction( opengl32, 'glClear', None, (GLbitfield,) )

glLoadIdentity = CreateDllFunction( opengl32, 'glLoadIdentity', None, noParams )

glLightfvParams = (c_uint, c_uint, POINTER(c_float))
glLightfv = CreateDllFunction( opengl32, 'glLightfv', None, glLightfvParams )

glRotatefParams = (c_float, c_float, c_float, c_float)
glRotatef = CreateDllFunction( opengl32, 'glRotatef', None, glRotatefParams )

glColor3fParams = (c_float, c_float, c_float)
glColor3f = CreateDllFunction( opengl32, 'glColor3f', None, glColor3fParams )

glBegin = CreateDllFunction( opengl32, 'glBegin', None, (GLenum,) )

glEnd = CreateDllFunction( opengl32, 'glEnd', None, noParams )

glVertex3fParams = (c_float, c_float, c_float)
glVertex3f = CreateDllFunction( opengl32, 'glVertex3f', None, glVertex3fParams )

glNormal3fParams = (c_float, c_float, c_float)
glNormal3f = CreateDllFunction( opengl32, 'glNormal3f', None, glNormal3fParams )

glTranslatefParams  = (c_float, c_float, c_float)
glTranslatef = CreateDllFunction( opengl32, 'glTranslatef', None, glTranslatefParams )

glMatrixMode = CreateDllFunction( opengl32, 'glMatrixMode', None, (GLenum,) )

glViewportParams = (GLint, GLint, GLsizei, GLsizei)
glViewport = CreateDllFunction( opengl32, 'glViewport', None, glViewportParams )

glEnable = CreateDllFunction( opengl32, 'glEnable', None, (GLenum,) )

glClearDepth = CreateDllFunction( opengl32, 'glClearDepth', None, (GLclampd,) )

glCullFace = CreateDllFunction(opengl32, 'glCullFace', None, (GLenum,))

glFrontFace = CreateDllFunction(opengl32, 'glFrontFace', None, (GLenum,))

glDepthMask = CreateDllFunction(opengl32, 'glDepthMask', None, (GLboolean,))

glDepthRange = CreateDllFunction(opengl32, 'glDepthRange', None, (GLclampd, GLclampd,))

# newer ones start here
glGenLists = CreateDllFunction( opengl32, 'glGenLists', GLuint, (GLsizei,) )

glNewList = CreateDllFunction( opengl32, 'glNewList', None, (GLuint, GLenum) )

glPushClientAttrib = CreateDllFunction( opengl32, 'glPushClientAttrib', None, (GLbitfield,) )

glEnableClientState = CreateDllFunction( opengl32, 'glEnableClientState', None, (GLenum,) )

glVertexPointerParams = (GLint, GLenum, GLsizei, POINTER(GLvoid))
glVertexPointer = CreateDllFunction( opengl32, 'glVertexPointer', None, glVertexPointerParams )

glNormalPointerParams = (GLenum, GLsizei, POINTER(GLvoid))
glNormalPointer = CreateDllFunction( opengl32, 'glNormalPointer', None, glNormalPointerParams )

glDrawElementsParams = (GLenum, GLsizei, GLenum, POINTER(GLvoid))
glDrawElements = CreateDllFunction( opengl32, 'glDrawElements', None, glDrawElementsParams )

glPopClientAttrib = CreateDllFunction( opengl32, 'glPopClientAttrib', None, noParams )

glEndList = CreateDllFunction( opengl32, 'glEndList', None, noParams )

glCallList = CreateDllFunction( opengl32, 'glCallList', None, (GLuint,) )

glShadeModel = CreateDllFunction( opengl32, 'glShadeModel', None, (GLenum,) )

glDepthFunc = CreateDllFunction( opengl32, 'glDepthFunc', None, (GLenum,) )

glHint = CreateDllFunction( opengl32, 'glHint', None, (GLenum, GLenum) )

# glDrawArrays = CreateDllFunction( opengl32, 'glDrawArrays', None, (GLenum, GLint, GLsizei) )
