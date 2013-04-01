# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ctypes import *

c_ptrdiff_t = c_ssize_t

GLenum = c_uint
GLbitfield = c_uint
GLuint = c_uint
GLint = c_int
GLsizei = c_int
GLboolean = c_ubyte
GLbyte = c_char
GLshort = c_short
GLubyte = c_ubyte
GLushort = c_ushort
GLulong = c_ulong
GLfloat = c_float
GLclampf = c_float
GLdouble = c_double
GLclampd = c_double
GLvoid = None
GLchar = c_char

GLintptr = c_ptrdiff_t
GLsizeiptr = c_ptrdiff_t

GLhandleARB = c_uint
GLcharARB = c_char

GLhalfARB = c_ushort
GLhalfNV = c_ushort