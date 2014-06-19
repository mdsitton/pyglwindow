import ctypes as ctypes

import src.library.x11 as x11

class Display(object):
	def get_monitors(self):
		return None, None

	def get_current_monitor(self, xPos, yPos):
		return None

	def get_monitor_resolution(self, screenNum):
		return None

	def set_monitor_resolution(self, width, height, monitor):
		pass

	def set_monitor_defaults(self):
		pass
