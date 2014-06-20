import platform

osName = platform.system()
if osName == 'Windows':
    from src.engine.window.win32 import Window
elif osName == 'Linux':
    from src.engine.window.x11 import Window
elif osName == 'Darwin':
    pass
else:
    pass