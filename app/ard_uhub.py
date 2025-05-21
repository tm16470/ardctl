#!/usr/bin/env python

import subprocess

def main():
  cmd = 'sudo uhubctl'
  subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()
