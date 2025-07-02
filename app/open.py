import subprocess
import re
import psutil
import os
import time
from logzero import logger

window_size = [
    {"width": 120, "height": 264},
    {"width": 200, "height": 440},
    {"width": 280, "height": 616},
]

def get_running_scrcpy_serials():
    serials = set()
    for proc in psutil.process_iter(['cmdline']):
        try:
            cmdline = proc.info['cmdline']
            if not cmdline:
                continue
            if any('scrcpy' in part for part in cmdline):
                if '-s' in cmdline:
                    idx = cmdline.index('-s') + 1
                    if idx < len(cmdline):
                        serials.add(cmdline[idx])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return serials

def run(args):
    n = 1
    if args.small_screen:
        n = 0
    if args.large_screen:
        n = 2

    window_width = window_size[n]["width"]
    window_height = window_size[n]["height"]

    connected = subprocess.check_output('adb devices -l', shell=True, text=True).split('\n')
    connected = [re.sub(r'[\s]+', ' ', line).strip() for line in connected if line.strip()]
    connected = [line.split(' ') for line in connected if 'device' in line]
    connected = [line for line in connected if line[1] == 'device']

    running_serials = get_running_scrcpy_serials()

    for device in connected:
        serial = device[0]
        if serial in running_serials:
            logger.info(f"scrcpy already running for {serial}, skipping.")
            continue

        model = next((part[6:] for part in device if part.startswith("model:")), serial[-4:])
        title = f"{model}_{serial[-4:]}"
        cmd = [
            "scrcpy", "-s", serial,
            "--stay-awake", "--no-audio",
            "--video-bit-rate", "128K",
            "--max-fps", "15",
            f"--window-title={title}",
            "--window-width", str(window_width),
            "--window-height", str(window_height)
        ]
        logger.info(f"Launching scrcpy for {serial} ({title}) with size {window_width}x{window_height}")
        if os.name == 'nt':
            proc = subprocess.Popen(
                ['cmd.exe', '/c'] + cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
        else:
            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        time.sleep(2.0)
        if proc.poll() is None:
            logger.info(f"scrcpy successfully launched for {serial}")
        else:
            logger.warning(f"scrcpy launch failed for {serial}")


