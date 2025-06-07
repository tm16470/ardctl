# ardctl: Android Recovery & Display CLI Tool

A Python CLI tool to manage Android devices via `adb`, launch `scrcpy` displays, align windows, send GUI swipe actions, and recover from `unauthorized` states using `uhubctl`.

## ⚡️ 構成構造

```
ardctl/
├── ardctl/
│   ├── __init__.py
│   ├── __main__.py
│   ├── open.py
│   ├── swipe.py
│   ├── align.py
│   └── recover.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

## 📄 `pyproject.toml`

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "ardctl"
version = "0.1.0"
description = "ADB & scrcpy automation toolkit"
authors = [
  {name = "Your Name", email = "your@email.com"}
]
dependencies = [
  "pywinctl",
  "pyautogui",
  "logzero",
  "tqdm"
]

[project.scripts]
ardctl = "ardctl.__main__:main"
```

## 📄 `requirements.txt`

```txt
pywinctl
pyautogui
logzero
tqdm
```

## 📗 `README.md`

```markdown
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
git clone https://github.com/yourname/ardctl.git
cd ardctl
pip install .
```

> Requires: `adb`, `scrcpy`, and `uhubctl` installed & configured
```

