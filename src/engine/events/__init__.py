
import platform

osName = platform.system()
if osName == 'Windows':
	from src.engine.events.win32 import Events
elif osName == 'Linux':
	from src.engine.events.x11 import Events
elif osName == 'Darwin':
	pass
else:
	pass 