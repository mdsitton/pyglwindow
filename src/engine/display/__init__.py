import platform

osName = platform.system()
if osName == 'Windows':
    from src.engine.display.win32 import Display
elif osName == 'Linux':
    from src.engine.display.x11 import Display
elif osName == 'Darwin':
    pass
else:
    pass