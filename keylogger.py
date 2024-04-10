import pynput
from pynput.keyboard import Key, Listener
import logging

def onPress(key):
    logging.info(str(key))
    with Listener(on_press=onPress) as listener:
        listener.join()