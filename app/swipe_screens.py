#!/usr/bin/env python3

import pywinctl
import pyautogui
import time
import sys
from logzero import logger
from tqdm import tqdm
import math
import platform

second_per_unit = 0.25
total_wait_second = 14
os_type = platform.system().lower()
pyautogui.FAILSAFE = False

def main():
    if len(sys.argv) > 1:
        loop = int(sys.argv[1])

    else:
        loop = 1

    coordinate = get_coordinate(loop)

    count = 1
    while True:
        for n in range(loop):
            logger.info(f"count {count}: {n + 1}: swiping...")
            pyautogui.moveTo(coordinate[n][0],coordinate[n][1])
            pyautogui.mouseDown()
            pyautogui.moveTo(coordinate[n][0],coordinate[n][2])
            pyautogui.mouseUp()
            time.sleep(second_per_unit)
        wait_second = math.ceil( total_wait_second - ( second_per_unit * loop ) )
        for i in tqdm(range(wait_second)):
            time.sleep(1)
            pass

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

if __name__ == "__main__":
    main()

