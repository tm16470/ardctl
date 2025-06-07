import pywinctl
import pyautogui
import time
import platform
import math
from logzero import logger
from tqdm import tqdm

second_per_unit = 0.1
total_wait_second = 10
os_type = platform.system().lower()
pyautogui.FAILSAFE = False

def run(args=None):
    loop = args.count or 1
    coordinate = get_coordinate(loop)
    count = 1

    while True:
        for n in range(loop):
            logger.info(f"count {count}: {n + 1}: swiping...")
            pyautogui.moveTo(coordinate[n][0], coordinate[n][1])
            pyautogui.mouseDown()
            pyautogui.moveTo(coordinate[n][0], coordinate[n][2])
            pyautogui.mouseUp()
            time.sleep(second_per_unit)

        wait_second = max(0, math.ceil(total_wait_second - (second_per_unit * loop)))
        for _ in tqdm(range(wait_second)):
            time.sleep(1)

        count += 1

def get_coordinate(loop):
    coordinate = []
    scrcpy_windows = pywinctl.getAllWindowsDict().get('scrcpy', {}).get('windows', {})

    for win in scrcpy_windows.values():
        window_size = win["size"]
        break
    else:
        raise RuntimeError("No scrcpy window found")

    for i in range(loop):
        if os_type == "linux":
            window_width = window_size.width
            window_height = window_size.height
        elif os_type == "darwin":
            window_width = window_size[0]
            window_height = window_size[1]

        if i == 0:
            x = int(window_width / 2)
            y = int(window_height / 2) + 37
            z = int(window_height) - 50
        else:
            if i % 2 == 0:
                x += window_width
                y = int(window_height / 2) + 37
                z = int(window_height) - 50
            else:
                y = 37 + window_height + 37 + int(window_height / 2)
                z = 37 + window_height

        coordinate.append([x, y, z])

    return coordinate
