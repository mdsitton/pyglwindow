# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ctypes import *
from ctypes.wintypes import *

from src.engine.bindings.util import CreateFunction

HGLRC = HANDLE

_wglCreateContextAttribsARBParams = (HDC, HGLRC, POINTER(c_int))
wglCreateContextAttribsARB = CreateFunction( 'wglCreateContextAttribsARB', HGLRC, _wglCreateContextAttribsARBParams )