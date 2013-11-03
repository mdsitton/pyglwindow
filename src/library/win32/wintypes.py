import ctypes
import sys

if sys.maxsize > 2 ** 32:
    arch = '64'
else:
    arch = '32'


def MAKEINTRESOURCE(i):
    return ctypes.cast(LPVOID(i & 0xFFFF), LPCWSTR)


def LOWORD(lParam):
    return ctypes.c_int16(lParam & 0xffff).value


def HIWORD(lParam):
    return ctypes.c_int16(lParam >> 16).value

# Types
INT = ctypes.c_int
UINT = ctypes.c_uint
BOOL = INT
if arch == '64':
    LONG_PTR = ctypes.c_longlong
    UINT_PTR = ctypes.c_ulonglong
    ULONG_PTR = ctypes.c_ulonglong
else:
    LONG_PTR = ctypes.c_long
    UINT_PTR = UINT
    ULONG_PTR = ctypes.c_ulong

VOID = None
ULONG = ctypes.c_ulong
WORD = ctypes.c_ushort
USHORT = ctypes.c_ushort
DWORD = ctypes.c_ulong
LPVOID = PVOID = ctypes.c_void_p
BYTE = ctypes.c_ubyte
LPARAM = LONG_PTR
LRESULT = LPARAM
LPARAM = LPARAM
WPARAM = UINT_PTR
WCHAR = ctypes.c_wchar
SHORT = ctypes.c_short
TCHAR = ctypes.c_wchar

# Handles
HANDLE = PVOID
HINSTANCE = HANDLE
HICON = HANDLE
HCURSOR = HANDLE
HMODULE = HANDLE
HBRUSH = HANDLE
HMENU = HANDLE
HWND = HANDLE
HMONITOR = HANDLE
HDC = HANDLE
HGDIOBJ = HANDLE

LPCWSTR = ctypes.c_wchar_p
LPCTSTR = LPCWSTR

ATOM = WORD
LONG = ctypes.c_long

WNDPROC = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)

POINTER = ctypes.POINTER


# Structures
class POINT(ctypes.Structure):
    _fields_ = [('x', LONG),
                ('y', LONG)]

POINTL = POINT

class WNDCLASS(ctypes.Structure):
    _fields_ = [('style', UINT),
                ('lpfnWndProc', WNDPROC),
                ('cbClsExtra', INT),
                ('cbWndExtra', INT),
                ('hInstance', HINSTANCE),
                ('hIcon', HICON),
                ('hCursor', HCURSOR),
                ('hbrBackground', HBRUSH),
                ('lpszMenuName', LPCTSTR),
                ('lpszClassName', LPCTSTR)]


class PIXELFORMATDESCRIPTOR_(ctypes.Structure):
    _fields_ = [('nSize', WORD),
                ('nVersion', WORD),
                ('dwFlags', DWORD),
                ('iPixelType', BYTE),
                ('cColorBits', BYTE),
                ('cRedBits', BYTE),
                ('cRedShift', BYTE),
                ('cGreenBits', BYTE),
                ('cGreenShift', BYTE),
                ('cBlueBits', BYTE),
                ('cBlueShift', BYTE),
                ('cAlphaBits', BYTE),
                ('cAlphaShift', BYTE),
                ('cAccumBits', BYTE),
                ('cAccumRedBits', BYTE),
                ('cAccumGreenBits', BYTE),
                ('cAccumBlueBits', BYTE),
                ('cAccumAlphaBits', BYTE),
                ('cDepthBits', BYTE),
                ('cStencilBits', BYTE),
                ('cAuxBuffers', BYTE),
                ('iLayerType', BYTE),
                ('bReserved', BYTE),
                ('dwLayerMask', DWORD),
                ('dwVisibleMask', DWORD),
                ('dwDamageMask', DWORD)]

def PIXELFORMATDESCRIPTOR():
    pf = PIXELFORMATDESCRIPTOR_()
    pf.nSize = ctypes.sizeof(pf)
    return pf
                
class DISPLAY_DEVICE(ctypes.Structure):
    _fields_ = [('cb', DWORD),
                ('DeviceName', WCHAR*32),
                ('DeviceString', WCHAR*128),
                ('StateFlags', DWORD),
                ('DeviceID', WCHAR*128),
                ('DeviceKey', WCHAR*128)]

class _S(ctypes.Structure):
    _fields_ = [('dmOrientation', SHORT),
                ('dmPaperSize', SHORT),
                ('dmPaperLength', SHORT),
                ('dmPaperWidth', SHORT)]

class _U(ctypes.Union):
    _anonymous_ = ('s',)
	
    _fields_ = [('s', _S),
                ('dmPosition', POINTL)]

class _U2(ctypes.Union):
    _fields_ = [('dmDisplayFlags', DWORD),
                ('dmNup', DWORD)]
                
class DEVMODE(ctypes.Structure):
    _anonymous_ = ('u',
                   'u2')

    _fields_ = [('dmDeviceName', WCHAR*32),
                ('dmSpecVersion', WORD),
                ('dmDriverVersion', WORD),
                ('dmSize', WORD),
                ('dmDriverExtra', WORD),
                ('dmFields', DWORD),
                ('u', _U),
                ('dmScale', SHORT),
                ('dmCopies', SHORT),
                ('dmDefaultSource', SHORT),
                ('dmPrintQuality', SHORT),
                ('dmColor', SHORT),
                ('dmDuplex', SHORT),
                ('dmYResolution', SHORT),
                ('dmTTOption', SHORT),
                ('dmCollate', SHORT),
                ('dmFormName', WCHAR*32),
                ('dmLogPixels', WORD),
                ('dmBitsPerPel', DWORD),
                ('dmPelsWidth', DWORD),
                ('dmPelsHeight', DWORD),
                ('u2', _U2),
                ('dmDisplayFrequency', DWORD),
                ('dmICMMethod', DWORD),
                ('dmICMIntent', DWORD),
                ('dmMediaType', DWORD),
                ('dmDitherType', DWORD),
                ('dmReserved1', DWORD),
                ('dmReserved2', DWORD),
                ('dmPanningWidth', DWORD),
                ('dmPanningHeight', DWORD)]


class RECT(ctypes.Structure):
    _fields_ = [('left', LONG),
                ('top', LONG),
                ('right', LONG),
                ('bottom', LONG)]

class MONITORINFOEX(ctypes.Structure):
    _fields_ = [('cbSize', DWORD),
                ('rcMonitor', RECT),
                ('rcWork', RECT),
                ('dwFlags', DWORD),
                ('szDevice',TCHAR*32)]


class MSG(ctypes.Structure):
    _fields_ = [('hwnd', HWND),
                ('message', UINT),
                ('wParam', WPARAM),
                ('lParam', LPARAM),
                ('time', DWORD),
                ('pt', POINT)]

class RAWINPUTDEVICE(ctypes.Structure):
    _fields_ = [('usUsagePage', USHORT),
                ('usUsage', USHORT),
                ('dwFlags', DWORD),
                ('hwndTarget', HWND)]

PRAWINPUTDEVICE = LPRAWINPUTDEVICE = POINTER(RAWINPUTDEVICE)
LPCRECT = LPRECT = POINTER(RECT)
LPMSG = POINTER(MSG)
LPPOINT = POINTER(POINT)

MONITORENUMPROC = ctypes.WINFUNCTYPE(BOOL, HMONITOR, HDC, POINTER(RECT), LPARAM)
TIMERPROC = ctypes.WINFUNCTYPE(VOID, HWND, UINT, UINT_PTR, DWORD)
