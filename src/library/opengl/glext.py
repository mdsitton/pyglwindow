from src.engine.utils.bindinghelper import define_glext_func
from src.library.opengl.gltypes import *

GL_FRAMEBUFFER_EXT = 0x8D40
GL_RENDERBUFFER_EXT = 0x8D41
GL_DEPTH_ATTACHMENT_EXT = 0x8D00
GL_STENCIL_ATTACHMENT_EXT = 0x8D20

GL_COLOR_ATTACHMENT0_EXT = 0x8CE0
GL_COLOR_ATTACHMENT1_EXT = 0x8CE1
GL_COLOR_ATTACHMENT2_EXT = 0x8CE2
GL_COLOR_ATTACHMENT3_EXT = 0x8CE3
GL_COLOR_ATTACHMENT4_EXT = 0x8CE4
GL_COLOR_ATTACHMENT5_EXT = 0x8CE5
GL_COLOR_ATTACHMENT6_EXT = 0x8CE6
GL_COLOR_ATTACHMENT7_EXT = 0x8CE7
GL_COLOR_ATTACHMENT8_EXT = 0x8CE8
GL_COLOR_ATTACHMENT9_EXT = 0x8CE9
GL_COLOR_ATTACHMENT10_EXT = 0x8CEA
GL_COLOR_ATTACHMENT11_EXT = 0x8CEB
GL_COLOR_ATTACHMENT12_EXT = 0x8CEC
GL_COLOR_ATTACHMENT13_EXT = 0x8CED
GL_COLOR_ATTACHMENT14_EXT = 0x8CEE
GL_COLOR_ATTACHMENT15_EXT = 0x8CEF

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

_glBufferSubDataParams = (GLenum, GLintptr, GLsizeiptr, c_void_p)
glBufferSubData = define_glext_func('glBufferSubData', None, _glBufferSubDataParams)

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


# Uniforms
glUniform1f = define_glext_func( 'glUniform1f', None, (GLint, GLfloat))

glUniform2f = define_glext_func( 'glUniform2f', None, (GLint, GLfloat, GLfloat))

glUniform3f = define_glext_func( 'glUniform3f', None, (GLint, GLfloat, GLfloat, GLfloat))

glUniform4f = define_glext_func( 'glUniform4f', None, (GLint, GLfloat, GLfloat, GLfloat, GLfloat))

glUniform1i = define_glext_func( 'glUniform1i', None, (GLint, GLint))

glUniform2i = define_glext_func( 'glUniform2i', None, (GLint, GLint, GLint))

glUniform3i = define_glext_func( 'glUniform3i', None, (GLint, GLint, GLint, GLint))

glUniform4i = define_glext_func( 'glUniform4i', None, (GLint, GLint, GLint, GLint, GLint))

glUniform1ui = define_glext_func( 'glUniform1ui', None, (GLint, GLuint))

glUniform2ui = define_glext_func( 'glUniform2ui', None, (GLint, GLuint, GLuint))

glUniform3ui = define_glext_func( 'glUniform3ui', None, (GLint, GLuint, GLuint, GLuint))

glUniform4ui = define_glext_func( 'glUniform4ui', None, (GLint, GLuint, GLuint, GLuint, GLuint))

glUniform1fv = define_glext_func( 'glUniform1f', None, (GLint, POINTER(GLfloat)))

glUniform2fv = define_glext_func( 'glUniform2f', None, (GLint, POINTER(GLfloat), POINTER(GLfloat)))

glUniform3fv = define_glext_func( 'glUniform3f', None, (GLint, POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)))

glUniform4fv = define_glext_func( 'glUniform4f', None, (GLint, POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat), POINTER(GLfloat)))

glUniform1iv = define_glext_func( 'glUniform1i', None, (GLint, POINTER(GLint)))

glUniform2iv = define_glext_func( 'glUniform2i', None, (GLint, POINTER(GLint), POINTER(GLint)))

glUniform3iv = define_glext_func( 'glUniform3i', None, (GLint, POINTER(GLint), POINTER(GLint), POINTER(GLint)))

glUniform4iv = define_glext_func( 'glUniform4i', None, (GLint, POINTER(GLint), POINTER(GLint), POINTER(GLint), POINTER(GLint)))

glUniform1uiv = define_glext_func( 'glUniform1i', None, (GLint, POINTER(GLuint)))

glUniform2uiv = define_glext_func( 'glUniform2i', None, (GLint, POINTER(GLuint), POINTER(GLuint)))

glUniform3uiv = define_glext_func( 'glUniform3i', None, (GLint, POINTER(GLuint), POINTER(GLuint), POINTER(GLuint)))

glUniform4uiv = define_glext_func( 'glUniform4i', None, (GLint, POINTER(GLuint), POINTER(GLuint), POINTER(GLuint), POINTER(GLuint)))

glUniformMatrix2fv = define_glext_func( 'glUniformMatrix2fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix4fv = define_glext_func( 'glUniformMatrix4fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix3fv = define_glext_func( 'glUniformMatrix3fv', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))


glUniformMatrix4fvARB = define_glext_func( 'glUniformMatrix4fvARB', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

glUniformMatrix3fvARB = define_glext_func( 'glUniformMatrix3fvARB', None, (GLint, GLsizei, GLboolean, POINTER(GLfloat)))

# glDrawArrays = define_glext_func( 'glDrawArrays', None, (GLenum, GLint, GLsizei) )

glUniform1fARB = define_glext_func( 'glUniform1fARB', None, (GLint, GLfloat))



glBindVertexArray = define_glext_func( 'glBindVertexArray', None, (GLuint,) )

glGetBufferParameterivARB = define_glext_func('glGetBufferParameterivARB', None, (GLenum, GLenum, POINTER(GLint)))

glGenFramebuffersEXT = define_glext_func('glGenFramebuffersEXT', None, (GLsizei, POINTER(GLuint)))

glBindFramebufferEXT = define_glext_func('glBindFramebufferEXT', None, (GLenum, GLuint))

glFramebufferTexture1DEXT = define_glext_func('glFramebufferTexture2DEXT', None, (GLenum, GLenum, GLenum, GLuint, GLint))

glFramebufferTexture2DEXT = define_glext_func('glFramebufferTexture2DEXT', None, (GLenum, GLenum, GLenum, GLuint, GLint))

glFramebufferTexture3DEXT = define_glext_func('glFramebufferTexture2DEXT', None, (GLenum, GLenum, GLenum, GLuint, GLint, GLint))

glGenRenderbuffersEXT = define_glext_func('glGenRenderbuffersEXT', None, (GLsizei, POINTER(GLuint)))

glBindRenderbufferEXT = define_glext_func('glBindRenderbufferEXT', None, (GLenum, GLuint))

glRenderbufferStorageEXT = define_glext_func('glRenderbufferStorageEXT', None, (GLenum, GLenum, GLsizei, GLsizei))

glFramebufferRenderbufferEXT = define_glext_func('glFramebufferRenderbufferEXT', None, (GLenum, GLenum, GLenum, GLuint))

glGenerateMipmap = define_glext_func('glGenerateMipmap', None, (GLenum,))

