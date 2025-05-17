from setuptools import setup, find_packages

setup(
    name="android-ctrl",
    version="0.1.0",
    description="A CLI tool to manage Android screens and apps",
    packages=find_packages(),
    install_requires=[
        "fire",
        "pywinctl",
        "pyautogui",
        "logzero",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "ard-remove-apps=app.ard-remove-apps:main",
            "ard-open=app.ard-open:main",
            "ard-align=app.ard-align:main",
            "ard-swipe=app.ard-swipe:main",
        ],
    },
    python_requires=">=3.6",
)
