import picounicorn
import time


class UnicornDisplay:
    def __init__(self):
        picounicorn.init()
        self.width = picounicorn.get_width()
        self.height = picounicorn.get_height()
        self.pixels_current = [[[0, 0, 0]] * self.height for i in range(self.width)]
        self.pixels_virtual = [[[0, 0, 0]] * self.height for i in range(self.width)]

    def clear(self):
        self.pixels_virtual = [[[0, 0, 0]] * self.height for i in range(self.width)]
        return self

    def render(self):
        if self.pixels_current != self.pixels_virtual:
            self.pixels_current = self.pixels_virtual
            for x, row in enumerate(self.pixels_current):
                for y, pixel in enumerate(row):
                    r, b, g = pixel
                    picounicorn.set_pixel(x, y, r, g, b)
        return self

    def set_pixel(self, x, y, r, g, b):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels_virtual[x][y] = [r, g, b]
        return self

    def self_test(self):
        brightness = 20
        print(f'pico unicorn pack width: {self.width}, height: {self.height}')
        while True:
            # for x in range(self.width):
            #     for y in range(self.height):
            #         self\
            #             .clear()\
            #             .set_pixel(x, y, brightness, brightness, brightness)\
            #             .render()
            #         time.sleep(1.0 / 20)
            #
            # for x in range(self.width):
            #     for y in range(self.height):
            #         self\
            #             .clear()\
            #             .set_pixel(self.width - x, self.height - y, brightness, brightness, brightness)\
            #             .render()
            #         time.sleep(1.0 / 80)

            for x in range(self.width):
                self.clear()
                for y in range(self.height):
                    if y <= 3:
                        self.set_pixel(x, y, brightness, 0, 0)
                        self.set_pixel(x + 1, y, 0, brightness, 0)
                        self.set_pixel(x + 2, y, 0, 0, brightness)
                self.render()
                time.sleep(1.0 / 10)
            for x in range(self.width):
                self.clear()
                for y in range(self.height):
                    if y >= 3:
                        self.set_pixel(self.width - x, y, brightness, 0, 0)
                        self.set_pixel(self.width - x - 1, y, 0, brightness, 0)
                        self.set_pixel(self.width - x - 2, y, 0, 0, brightness)
                self.render()
                time.sleep(1.0 / 10)
