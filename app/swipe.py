import pywinctl
import pyautogui
import time
import platform
import math
import random
import subprocess
import re
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
    connected = subprocess.check_output('adb devices -l', shell=True, text=True).split('\n')
    connected = [re.sub(r'[\s]+', ' ', line).strip() for line in connected if line.strip()]
    connected = [line.split(' ') for line in connected if 'device' in line]
    connected = [line for line in connected if line[1] == 'device']

    titles = []
    for device in connected:
        serial = device[0]
        model = next((part[6:] for part in device if part.startswith("model:")), serial[-4:])
        title = f"{model}_{serial[-4:]}"
        titles.append(title)

    if not titles:
        logger.error("No connected devices found via adb.")
        exit(1)

    count = 0
    for title in titles:
        if limit and count >= limit:
            break
        try:
            win = pywinctl.getWindowsWithTitle(title)[0]
            box = win.getClientFrame()
            x = box.left + (box.right - box.left) // 2
            y_start = box.top + (box.bottom - box.top) // 2
            y_end = y_start + 100  # swipe downward
            coordinate.append([x, y_start, y_end])
            count += 1
        except Exception as e:
            logger.warning(f"Could not find scrcpy window '{title}': {e}")

    if not coordinate:
        logger.error("No scrcpy windows matched expected titles.")
        exit(1)

    return coordinate
