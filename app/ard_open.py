#!/usr/bin/env python

import argparse
import sys
import subprocess
import re

window_size = [
        { "width": 140, "height": 310 },
        { "width": 220, "height": 485 },
        { "width": 300, "height": 660 },
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--small-screen", action="store_true", default=False)
    parser.add_argument("-m", "--mid-screen", action="store_true", default=False)
    parser.add_argument("-l", "--large-screen", action="store_true", default=False)
    args = parser.parse_args()

    n = 1
    if args.small_screen == True:
        n = 0

    if args.large_screen == True:
        n = 2

    window_width = window_size[n]["width"]
    window_height = window_size[n]["height"]
    

# connected devices
    cmd = 'adb devices -l'
    connected = subprocess.check_output(cmd, shell=True, text=True)

    # make text, "connected", to list by return
    connected = connected.split('\n')

    # change multiple consecutive spaces or tab to one space
    connected = [re.sub(r'[\s]+', ' ', i)  for i in connected]

    # remove empty elments
    connected = [i for i in connected if not re.match(r'^\s*$', i)]

    # change connected to a list of lists
    connected = [i.split(' ') for i in connected]

    connected = [i for i in connected if i[1] == 'device']

# processing devices
    processing = list()
    cmd = 'ps -ef | grep "adb -s" | grep "CLASSPATH=/data/local/tmp/scrcpy-server.jar"' 
    proc = subprocess.check_output(cmd, shell=True, text=True)

    # make text, "processing", to list by return
    proc = proc.split('\n')
    
    # change multiple consecutive spaces or tab to one space
    proc = [re.sub(r'[\s]+', ' ', i)  for i in proc]

    proc = [re.sub(r'^[\s]+', '', i)  for i in proc]

    # pick up matching value
    for x in proc:
        y = x.split(' ')
        if len(y) > 9 and re.match('adb', y[7]) \
            and re.match('-s', y[8]) \
            and re.match('CLASSPATH=/data/local/tmp/scrcpy-server.jar', y[11]):
            processing.append(y[9])

# start scrcpy for devices connecting but not running.
    for i in connected:
        if not i[0] in processing: 
            cmd = (
                f'scrcpy -s {i[0]} '
                '--stay-awake '
                '--no-audio '
                '--video-bit-rate 128K '
                '--max-fps 15 '
                f'--window-title={i[4][6:]}_{i[0][-4:]} '
                f'--window-width {window_width} '
                f'--window-height {window_height} '
                '&'
            )
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
