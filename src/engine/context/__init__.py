import platform

osName = platform.system()
if osName == 'Windows':
    from src.engine.context.win32 import Context
elif osName == 'Linux':
    from src.engine.context.x11 import Context
elif osName == 'Darwin':
    pass
else:
    pass