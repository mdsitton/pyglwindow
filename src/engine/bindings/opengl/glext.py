# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from src.engine.bindings.util import CreateFunction
from src.engine.bindings.opengl.gltypes import *


# Used when a function has no params instead of the (), it looks cleaner.
noParams = ()

# OpenGL ARB function calls
glCreateShaderObjectARB = CreateFunction( 'glCreateShaderObjectARB', GLhandleARB, (GLenum,) )

glShaderSourceARB = CreateFunction( 'glShaderSourceARB', None, (GLhandleARB, GLsizei, POINTER(POINTER(GLcharARB)), POINTER(GLint)) )

glCompileShaderARB = CreateFunction( 'glCompileShaderARB', None, (GLhandleARB,) )

glCreateProgramObjectARB = CreateFunction( 'glCreateProgramObjectARB', GLhandleARB, () )

glAttachObjectARB = CreateFunction( 'glAttachObjectARB', None, (GLhandleARB, GLhandleARB) )

glLinkProgramARB = CreateFunction( 'glLinkProgramARB', None, (GLhandleARB,) )

glUseProgramObjectARB = CreateFunction( 'glUseProgramObjectARB', None, (GLhandleARB,) )

# OpenGL 3.3+ calls
glGenVertexArrays = CreateFunction( 'glGenVertexArrays', None, (GLsizei, POINTER(GLuint)) )

glBindVertexArray = CreateFunction ('glBindVertexArray', None, (GLuint,))

glDeleteVertexArrays = CreateFunction ('glDeleteVertexArrays', None, (GLsizei, POINTER(GLuint)))

glGenBuffers = CreateFunction( 'glGenBuffers', None, (GLsizei, POINTER(GLuint)) )

glDeleteBuffers = CreateFunction( 'glDeleteBuffers', None, (GLsizei, POINTER(GLuint)))

glBindBuffer = CreateFunction( 'glBindBuffer', None, (GLenum, GLuint) )

_glBufferDataParams = (GLenum, GLsizeiptr, c_void_p, GLenum)
glBufferData = CreateFunction( 'glBufferData', None, _glBufferDataParams )

glCreateShader = CreateFunction( 'glCreateShader', GLuint, (GLenum,) )

glShaderSource = CreateFunction( 'glShaderSource', None, (GLuint, GLsizei, POINTER(POINTER(GLchar)), POINTER(GLint)) )

glCompileShader = CreateFunction( 'glCompileShader', None, (GLuint,) )

glDeleteShader = CreateFunction( 'glDeleteShader', None, (GLuint,))

glCreateProgram = CreateFunction( 'glCreateProgram', GLuint, noParams )

glAttachShader = CreateFunction( 'glAttachShader', None, (GLuint, GLuint) )

glLinkProgram = CreateFunction( 'glLinkProgram', None, (GLuint,) )

glDetachShader = CreateFunction( 'glDetachShader', None, (GLuint, GLuint) )

glUseProgram = CreateFunction( 'glUseProgram', None, (GLuint,) )

glDeleteProgram = CreateFunction( 'glDeleteProgram', None, (GLuint,))

glBindBuffer = CreateFunction( 'glBindBuffer', None, (GLenum, GLuint) )

glEnableVertexAttribArray = CreateFunction( 'glEnableVertexAttribArray', None, (GLuint,) )

glVertexAttribPointer = CreateFunction( 'glVertexAttribPointer', None, (GLuint, GLint, GLenum, GLboolean, GLsizei, c_void_p) )

glDisableVertexAttribArray = CreateFunction( 'glDisableVertexAttribArray', None, (GLuint,) )

glGetShaderiv = CreateFunction( 'glGetShaderiv', None, (GLuint, GLenum, POINTER(GLint)) )

glGetShaderInfoLog = CreateFunction( 'glGetShaderInfoLog', None, (GLuint, GLsizei, POINTER(GLsizei), POINTER(GLchar)))

glGetProgramiv = CreateFunction( 'glGetProgramiv', None, (GLuint, GLenum, POINTER(GLint)) )

glGetUniformLocation = CreateFunction( 'glGetUniformLocation', GLint, (GLuint, POINTER(GLchar)))

glGetAttribLocation = CreateFunction('glGetUniformLocation', GLint, (GLhandleARB, POINTER(GLcharARB)))

glGetUniformLocationARB = CreateFunction( 'glGetUniformLocationARB', GLint, (GLhandleARB, POINTER(GLcharARB)))

glGetAttribLocationARB = CreateFunction('glGetUniformLocationARB', GLint, (GLhandleARB, POINTER(GLcharARB)))

glUniformMatrix4fv = CreateFunction( 'glUniformMatrix4fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix4fvARB = CreateFunction( 'glUniformMatrix4fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glDrawArrays = CreateFunction( 'glDrawArrays', None, (GLenum, GLint, GLsizei) )

glUniform1fARB = CreateFunction( 'glUniform1fARB', None, (GLint, GLfloat))

glBindVertexArray = CreateFunction( 'glBindVertexArray', None, (GLuint,) )

glGetBufferParameterivARB = CreateFunction('glGetBufferParameterivARB', None, (GLenum, GLenum, POINTER(GLint)))