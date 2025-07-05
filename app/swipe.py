import pywinctl
import pyautogui
import time
import platform
import math
import random
from logzero import logger
from tqdm import tqdm

second_per_unit = 0.1
pyautogui.FAILSAFE = False

def run(args=None):
    loop = args.count or 1
    coordinate = get_coordinates(loop)
    count = 1

    while True:
        for n in range(len(coordinate)):
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

def get_coordinates(limit):
    coordinate = []
    windows = [w for w in pywinctl.getAllWindows() if '_' in w.title and len(w.title) >= 5]

    count = 0
    for win in windows:
        if limit and count >= limit:
            break
        try:
            box = win.getClientFrame()
            x = box.left + (box.right - box.left) // 2
            y_start = box.top + (box.bottom - box.top) // 2
            y_end = box.top  # swipe to the top of the window
            coordinate.append([x, y_start, y_end])
            count += 1
        except Exception as e:
            logger.warning(f"Could not get window geometry for '{win.title}': {e}")

    if not coordinate:
        logger.error("No usable scrcpy windows found.")
        exit(1)

    return coordinate
