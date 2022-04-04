import time
import random


class Pause:

    def __init__(self, pause_array):
        self.pause_array = pause_array

    def create_pause_for_press_button(self):
        pause_time = random.randrange(166, 166 + 40, 1)
        self.check_pause_array(pause_time)
        if len(self.pause_array) < 29:
            self.create_pause_for_press_button()
        else:
            result = self.pause_array
            return result

    def check_pause_array(self, pause_time):
        if pause_time in self.pause_array:
            pause_time = random.randrange(166, 166 + 40, 1)
            self.check_pause_array(pause_time)
        else:
            self.pause_array.append(pause_time/1000)

    def get_pause_array_for_button(self):
        return self.create_pause_for_press_button()


if __name__ == '__main__':
    a = Pause([])
    print(a.get_pause_array_for_button())
