import pyautogui
import time
import random
from .pause import Pause


class Buttons(Pause):


    def press_button(self):
        pyautogui.press(f'{self}')
        time.sleep(self.)



