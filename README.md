
# ardctl

A command-line tool to manage Android device display/control using `adb`, `scrcpy`, and `uhubctl`.

## Features
- `ardctl open`: Launch `scrcpy` sessions for connected devices not already active
- `ardctl align`: Arrange all scrcpy windows on screen
- `ardctl swipe`: Simulate swipe-down on scrcpy windows via `pyautogui`
- `ardctl recover`: Auto-recover `unauthorized` devices by toggling USB ports with `uhubctl`

## Usage

```bash
# Launch scrcpy for connected devices
ardctl open

# Arrange scrcpy windows
ardctl align

# Swipe loop
ardctl swipe -c 2

# Recover unauthorized devices
ardctl recover
```

## Setup

```bash
git clone https://github.com/tm16470/ardctl.git
cd ardctl
pip install .
```

> Requires: `adb`, `scrcpy`, and `uhubctl` installed & configured
```

