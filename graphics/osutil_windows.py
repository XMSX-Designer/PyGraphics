from win32api import GetSystemMetrics

class display:
    
    @staticmethod
    def getsize():
        return GetSystemMetrics(0),GetSystemMetrics(1)
        