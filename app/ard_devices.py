#!/usr/bin/env python

import subprocess

def main():
  cmd = 'adb devices'
  subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
