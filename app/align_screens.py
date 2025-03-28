#!/usr/bin/env python

import argparse
import pywinctl

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--small-screen", action="store_true", default=False
    )
    args = parser.parse_args()
    
    screens = pywinctl.getAllWindowsDict()['scrcpy']['windows']
    
    position = get_position(screens)
    
    c = 0
    for x in pywinctl.getAllWindowsDict()['scrcpy']['windows'].keys():
        w = pywinctl.getWindowsWithTitle(x)
        w[0].moveTo(position[c][0], position[c][1])

        c += 1


def get_position(screens):
    position = list()

    for i in screens:
        window_size = screens[i]["size"]
        break

    x, y = 0, 0
    for i, j in enumerate(screens):
        if i == 0:
            pass

        elif i == 1:
            y = window_size.height + 37
        
        else:
            if i % 2 == 0:
                x = x + window_size.width
                y = 0
            else:
                y = window_size.height + 37

        position.append([x, y])

    return position


if __name__ == "__main__":
    main()
