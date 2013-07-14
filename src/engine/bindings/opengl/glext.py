
from src.engine.utils.bindinghelper import define_glext_func
from src.engine.bindings.opengl.gltypes import *


# Used when a function has no params instead of the (), it looks cleaner.
noParams = ()

# OpenGL ARB function calls
glCreateShaderObjectARB = define_glext_func( 'glCreateShaderObjectARB', GLhandleARB, (GLenum,) )

glShaderSourceARB = define_glext_func( 'glShaderSourceARB', None, (GLhandleARB, GLsizei, POINTER(POINTER(GLcharARB)), POINTER(GLint)) )

glCompileShaderARB = define_glext_func( 'glCompileShaderARB', None, (GLhandleARB,) )

glCreateProgramObjectARB = define_glext_func( 'glCreateProgramObjectARB', GLhandleARB, () )

glAttachObjectARB = define_glext_func( 'glAttachObjectARB', None, (GLhandleARB, GLhandleARB) )

glLinkProgramARB = define_glext_func( 'glLinkProgramARB', None, (GLhandleARB,) )

glUseProgramObjectARB = define_glext_func( 'glUseProgramObjectARB', None, (GLhandleARB,) )

# OpenGL 3.3+ calls
glGenVertexArrays = define_glext_func( 'glGenVertexArrays', None, (GLsizei, POINTER(GLuint)) )

glBindVertexArray = define_glext_func ('glBindVertexArray', None, (GLuint,))

glDeleteVertexArrays = define_glext_func ('glDeleteVertexArrays', None, (GLsizei, POINTER(GLuint)))

glGenBuffers = define_glext_func( 'glGenBuffers', None, (GLsizei, POINTER(GLuint)) )

glDeleteBuffers = define_glext_func( 'glDeleteBuffers', None, (GLsizei, POINTER(GLuint)))

glBindBuffer = define_glext_func( 'glBindBuffer', None, (GLenum, GLuint) )

_glBufferDataParams = (GLenum, GLsizeiptr, c_void_p, GLenum)
glBufferData = define_glext_func( 'glBufferData', None, _glBufferDataParams )

glCreateShader = define_glext_func( 'glCreateShader', GLuint, (GLenum,) )

glShaderSource = define_glext_func( 'glShaderSource', None, (GLuint, GLsizei, POINTER(POINTER(GLchar)), POINTER(GLint)) )

glCompileShader = define_glext_func( 'glCompileShader', None, (GLuint,) )

glDeleteShader = define_glext_func( 'glDeleteShader', None, (GLuint,))

glCreateProgram = define_glext_func( 'glCreateProgram', GLuint, noParams )

glAttachShader = define_glext_func( 'glAttachShader', None, (GLuint, GLuint) )

glLinkProgram = define_glext_func( 'glLinkProgram', None, (GLuint,) )

glDetachShader = define_glext_func( 'glDetachShader', None, (GLuint, GLuint) )

glUseProgram = define_glext_func( 'glUseProgram', None, (GLuint,) )

glDeleteProgram = define_glext_func( 'glDeleteProgram', None, (GLuint,))

glBindBuffer = define_glext_func( 'glBindBuffer', None, (GLenum, GLuint) )

glEnableVertexAttribArray = define_glext_func( 'glEnableVertexAttribArray', None, (GLuint,) )

glVertexAttribPointer = define_glext_func( 'glVertexAttribPointer', None, (GLuint, GLint, GLenum, GLboolean, GLsizei, c_void_p) )

glDisableVertexAttribArray = define_glext_func( 'glDisableVertexAttribArray', None, (GLuint,) )

glGetShaderiv = define_glext_func( 'glGetShaderiv', None, (GLuint, GLenum, POINTER(GLint)) )

glGetShaderInfoLog = define_glext_func( 'glGetShaderInfoLog', None, (GLuint, GLsizei, POINTER(GLsizei), POINTER(GLchar)))

glGetProgramiv = define_glext_func( 'glGetProgramiv', None, (GLuint, GLenum, POINTER(GLint)) )

glGetUniformLocation = define_glext_func( 'glGetUniformLocation', GLint, (GLuint, POINTER(GLchar)))

glGetAttribLocation = define_glext_func('glGetUniformLocation', GLint, (GLhandleARB, POINTER(GLcharARB)))

glGetUniformLocationARB = define_glext_func( 'glGetUniformLocationARB', GLint, (GLhandleARB, POINTER(GLcharARB)))

glGetAttribLocationARB = define_glext_func('glGetUniformLocationARB', GLint, (GLhandleARB, POINTER(GLcharARB)))

glUniformMatrix4fv = define_glext_func( 'glUniformMatrix4fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix3fv = define_glext_func( 'glUniformMatrix3fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix4fvARB = define_glext_func( 'glUniformMatrix4fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix3fvARB = define_glext_func( 'glUniformMatrix3fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

# glDrawArrays = define_glext_func( 'glDrawArrays', None, (GLenum, GLint, GLsizei) )

glUniform1fARB = define_glext_func( 'glUniform1fARB', None, (GLint, GLfloat))

glBindVertexArray = define_glext_func( 'glBindVertexArray', None, (GLuint,) )

glGetBufferParameterivARB = define_glext_func('glGetBufferParameterivARB', None, (GLenum, GLenum, POINTER(GLint)))