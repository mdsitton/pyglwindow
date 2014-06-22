
class Context(object):
    ''' Creates and returns an OpenGL Context of the requested version '''

    def __init__(self, oglVersion):

        # Seperate the opengl version into major and minor
        self.major, self.minor = (int(item) for item in str(oglVersion).split('.'))

    def _create(self):
        ''' Called from window code once all values have been set from game code '''
        pass

    def _define_pixel_format(self, color=32, depth=24, stencil=8):
        ''' Defines a new pixel format descriptor '''

        return None

    def delete(self):
        ''' Delete's the context '''
        pass
