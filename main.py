import time
from rpi_ws281x import PixelStrip, Color, ws

# LED strip configuration:
LED_COUNT = 50        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP_TYPE = ws.WS2811_STRIP_RGB

class OutdoorLights(PixelStrip):
    led_count = 50        
    led_pin = 18          
    led_freq_hz = 800000  
    led_dma = 10          
    led_brightness = 250  
    led_invert = False    
    led_channel = 0       
    led_strip_type = ws.WS2811_STRIP_RGB

    def __init__(self):
        super().__init__(
            num=self.led_count, 
            pin=self.led_pin, 
            freq_hz=self.led_freq_hz, 
            dma=self.led_dma, 
            invert=self.led_invert,
            brightness=self.led_brightness, 
            channel=self.led_channel, 
            strip_type=self.led_strip_type, 
            gamma=None
            )

    def swipe(self, color: Color, ms_delay: int = 1000):
        for i in range(self.led_count):
            lights.setPixelColor(i,color)
            lights.show()
            time.sleep(ms_delay/1000)


lights=OutdoorLights()

lights.begin()

while True:
    lights.swipe(color=Color(150,0,200), ms_delay=15)
    lights.swipe(color=Color(255,50,0), ms_delay=15)
