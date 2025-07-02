import pywinctl
import subprocess
import re
from logzero import logger

def run(args=None):
    connected = subprocess.check_output('adb devices -l', shell=True, text=True).split('\n')
    connected = [re.sub(r'[\s]+', ' ', line).strip() for line in connected if line.strip()]
    connected = [line.split(' ') for line in connected if 'device' in line]
    connected = [line for line in connected if line[1] == 'device']

    expected_titles = []
    for device in connected:
        serial = device[0]
        model = next((part[6:] for part in device if part.startswith("model:")), serial[-4:])
        title = f"{model}_{serial[-4:]}"
        expected_titles.append(title)

    logger.info(f"Looking for window titles: {expected_titles}")

    windows = []
    for title in expected_titles:
        try:
            win = pywinctl.getWindowsWithTitle(title)[0]
            windows.append(win)
        except Exception as e:
            logger.warning(f"Could not find window '{title}': {e}")

    if not windows:
        logger.warning("No matching scrcpy windows found.")
        return

    windows.sort(key=lambda w: w.title)
    position = get_position(len(windows))

    for i, win in enumerate(windows):
        logger.info(f"Aligning: '{win.title}' → X:{position[i][0]} Y:{position[i][1]}")
        try:
            win.moveTo(position[i][0], position[i][1])
        except Exception as e:
            logger.warning(f"Failed to move '{win.title}': {e}")

def get_position(count):
    position = []
    x, y = 0, 0
    width, height = 200, 440  # Default size used in open.py

    for i in range(count):
        if i == 0:
            pass
        elif i == 1:
            y = height + 37
        else:
            if i % 2 == 0:
                x += width
                y = 0
            else:
                y = height + 37
        position.append([x, y])
    return position
