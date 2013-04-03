# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from src.engine.bindings.win32 import *
from src.engine.bindings.opengl.wgl import *
from src.engine.context import Context


class TempContext(object):
    def __init__(self):

        def wnd_proc(hwnd, message, wParam, lParam):
            return DefWindowProc(hwnd, message, wParam, lParam)

        # create window class
        wndClass = WNDCLASS()
        wndClass.style = CS_HREDRAW | CS_VREDRAW | CS_OWNDC
        wndClass.lpfnWndProc = WNDPROC(wnd_proc)
        wndClass.cbClsExtra = 0
        wndClass.cbWndExtra = 0
        wndClass.hInstance = 0
        wndClass.hIcon = LoadIcon(None, IDI_INFORMATION)
        wndClass.hCursor = LoadCursor(None, IDC_ARROW)
        wndClass.hbrBackground = None
        wndClass.lpszMenuName = None
        wndClass.lpszClassName = 'tempContext'

        # Register class
        RegisterClass(pointer(wndClass))

        dwStyle = (WS_OVERLAPPEDWINDOW |
                   WS_CLIPSIBLINGS |
                   WS_CLIPCHILDREN)

        # Create window
        self.hwnd = CreateWindowEx(WS_EX_APPWINDOW, wndClass.lpszClassName,
                    'tempContext', dwStyle, CW_USEDEFAULT, CW_USEDEFAULT, 0, 0,
                     None, None, wndClass.hInstance, None)

        self.context = Context(self.hwnd, 2.1)

    def get_hwnd():
        return self.hwnd

    def delete(self):
        ''' Delete the temp window and context '''
        self.context.delete()
        # DestroyWindow(self.hwnd)