import picounicorn
import time


class UnicornDisplay:
    def __init__(self):
        picounicorn.init()
        self.width = picounicorn.get_width()
        self.height = picounicorn.get_height()

    def self_test(self):
        brightness = 50
        blinking = False
        tick = 0

        while True:
            if picounicorn.is_pressed(picounicorn.BUTTON_X) and brightness + 5 < 255:
                brightness += 5
            if picounicorn.is_pressed(picounicorn.BUTTON_Y) and brightness - 5 > 0:
                brightness -= 5
            if picounicorn.is_pressed(picounicorn.BUTTON_A):
                blinking = True
                tick = 1
            if picounicorn.is_pressed(picounicorn.BUTTON_B):
                blinking = False
                tick = 1

            if blinking and tick % 10 == 0:
                for x in range(self.width):
                    for y in range(self.height):
                        picounicorn.set_pixel(x, y, 0, 0, 0)
                tick = 0
            else:
                for x in range(self.width):
                    for y in range(self.height):
                        picounicorn.set_pixel(x, y, brightness, brightness, brightness)

            tick += 1

            time.sleep(1.0 / 60)

