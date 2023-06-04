from Interface import Interface

class Mock(Interface):
    def getLatitudLongitud(self, ciudad, pais):
        return 123, 789
