import time
from config import outdoor_lights
from rpi_ws281x import PixelStrip, Color, ws

LED_STRIP_TYPE = ws.WS2811_STRIP_RGB

class WS211(PixelStrip):    
    type = ws.WS2811_STRIP_RGB

    def __init__(self, **kwargs):
        super().__init__(**kwargs,LED_STRIP_TYPE=self.type)

    def swipe(self, color: Color, ms_delay: int = 1000):
        for i in range(self.led_count):
            lights.setPixelColor(i,color)
            lights.show()
            time.sleep(ms_delay/1000)
    
    def wipe(self):
        for i in range(self.led_count):
            self.setPixelColor(i,Color(0,0,0,0))
        self.show()    
        self._cleanup()
    
    def skip(self, primary:Color, skipper: Color, ms_delay:int = 1000):
        while True:
            prev = 0
            for i in range(self.led_count):
                if i == 0:
                    self.setPixelColor(i,skipper)
                    self.show()
                else:
                    self.setPixelColor(i-1,primary)
                    self.setPixelColor(i,skipper)
                    self.show()
                    time.sleep(ms_delay/1000)
                    self.setPixelColor(i,primary)


lights=WS211(**outdoor_lights)

lights.begin()

lights.skip(primary=Color(150,0,200), skipper=Color(255,50,0), ms_delay=150)
