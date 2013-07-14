import ctypes as ct
import src.engine.bindings.win32 as w32

class Display(object):
    
    def get_monitors(self):

        # Get each monitor and put it into a list
        monitors = []

        def disp_proc(hMonitor, hdcMonitor, lprcMonitor, dwData):
            lprcMonitor = lprcMonitor.contents
            if lprcMonitor.left == 0 and lprcMonitor.top == 0:
                primary = True
            else:
                primary = False

            monitors.append({
                'rect': {
                    'right': lprcMonitor.right,
                    'left': lprcMonitor.left,
                    'top': lprcMonitor.top,
                    'bottom': lprcMonitor.bottom,
                },
                'handle': hMonitor,
                'primary': primary})
            return True

        dispProc = w32.MONITORENUMPROC(disp_proc)
        w32.EnumDisplayMonitors(None, None, dispProc, 0)

        monitorInfo = []
        monitorCount = 0
        for n, mon in enumerate(monitors):
            monitorInfo.append({
                'rect': mon['rect'],
                'handle': mon['handle'],
                'primary': mon['primary'],
                'resolution': {
                    'width': mon['rect']['right'] - mon['rect']['left'],
                    'height': mon['rect']['bottom'] - mon['rect']['top'],
                    'offset': {
                        'x': mon['rect']['left'],
                        'y': mon['rect']['top'],
                    },
                },
            })

            monitorCount += 1

        return monitorInfo, monitorCount

    def get_current_monitor(self, xPos, yPos):
        """ Returns a monitor based on a single point need to change name of func """
        monitorFound = 0
        for i, monitor in enumerate(self.monitorInfo):
            monRect = monitor['rect']
            if xPos <= monRect['right'] and xPos >= monRect['left']:
                if yPos <= monRect['bottom'] and yPos >= monRect['top']:
                    monitorFound = i

        return monitorFound

    def get_monitor_resolution(self, screenNum):
        """Get the resolution for the specified display."""

        # Select the specified display.
        resolution = self.monitorInfo[screenNum]['resolution']

        return resolution

    def set_monitor_resolution(self, width, height, monitor):
        ''' Changes the resolution of the monitor selected
            This should not be used for the most part
            We do not want to ever change any screen's resolution
            It takes about 3 seconds for the resolution to change
            which is just to long
        '''
        displayDevices = []

        for n in range(self.monitorCount):
            displayDevices.append(w32.MONITORINFOEX())
            w32.GetMonitorInfo(self.monitorInfo[monitor]['handle'],
                               ct.pointer(displayDevices[n]))

        screenMode = w32.DEVMODE()

        w32.EnumDisplaySettings(displayDevices[monitor].szDevice,
                                  w32.ENUM_CURRENT_SETTINGS,
                                  ct.pointer(screenMode))

        screenMode.dmSize = ct.sizeof(screenMode)
        screenMode.dmPelsWidth = width
        screenMode.dmPelsHeight = height
        screenMode.dmBitsPerPel = 32
        screenMode.dmFields = (w32.DM_PELSWIDTH |
                               w32.DM_PELSHEIGHT |
                               w32.DM_BITSPERPEL)

        w32.ChangeDisplaySettings(ct.pointer(screenMode), w32.CDS_FULLSCREEN)

        self.monitorInfo, self.monitorCount = self.get_monitors()

    def set_monitor_defaults(self):
        w32.ChangeDisplaySettings(None, w32.CDS_FULLSCREEN)
        self.monitorInfo, self.monitorCount = self.get_monitors()