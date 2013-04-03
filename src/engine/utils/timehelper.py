# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import platform
import time
import math

# Clock on Unix systems is not accurate and only counts program running time
# On windows it counts all time
# But time isnt as good as clock on windows
# If we move to python 3.3+ we can move to solely time.monotonic()
# If time is not monitonic the timer could get negitive delta values (bad)
if platform.system() == 'Windows':
    timeFunc = time.clock
else:
    timeFunc = time.time


class Timer(object):
    def __init__(self):
        self.startTime = None  # Time is given in seconds i want miliseconds

        self.currentTime = None
        self.previousTime = None

        self.tickDelta = None

    def tick(self):
        ''' Returns the delta between the current and previous ticks '''

        if self.currentTime is not None:
            self.previousTime = self.currentTime

        self.currentTime = timeFunc() * 1000

        if self.previousTime is not None:
            self.tickDelta = self.currentTime - self.previousTime
        else:
            self.tickDelta = 0

        if self.tickDelta < 0:
            print "88 mph nice!"

        return self.tickDelta