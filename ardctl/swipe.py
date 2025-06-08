cat ardctl/swipe.py
import pywinctl
import pyautogui
import time
import platform
import math
import random
from logzero import logger
from tqdm import tqdm

second_per_unit = 0.1
os_type = platform.system().lower()
pyautogui.FAILSAFE = False

def run(args=None):
    loop = args.count or 1
    coordinate = get_coordinate(loop)
    count = 1

    while True:
        for n in range(loop):
            x = coordinate[n][0]
            y_start = coordinate[n][1]
            y_end = coordinate[n][2]
            logger.info(f"count {count}: {n + 1}: swiping from ({x}, {y_start}) to ({x}, {y_end})")
            pyautogui.moveTo(x, y_start)
            pyautogui.mouseDown()
            pyautogui.moveTo(x, y_end)
            pyautogui.mouseUp()
            time.sleep(second_per_unit)

        wait_second = round(random.uniform(10.0, 12.0), 1)
        logger.info(f"Waiting {wait_second} seconds before next swipe set...")
        for _ in tqdm(range(int(wait_second * 10))):
            time.sleep(0.1)

        count += 1

def get_coordinate(loop):
    coordinate = list()

    screens = pywinctl.getAllWindowsDict()['scrcpy']['windows']
    for i in screens:
        window_size = screens[i]["size"]
        break

    x, y, z = 0, 0, 0
    for i in range(loop):
        if os_type == "linux":
            window_width = window_size.width
            window_height = window_size.height
        elif os_type == "darwin":
            window_width = window_size[0]
            window_height = window_size[1]

        if i == 0:
            x = int(window_width / 2)
            y = int(window_height / 2 ) + 37
        else:
            if i % 2 == 0:
                x = x + window_width
                y = int(window_height / 2 ) + 37
                z = 0
            else:
                y = 37 + window_height + 37 + int(window_height / 2)
                z = 37 + window_height

        coordinate.append([x, y, z])

    return coordinate
