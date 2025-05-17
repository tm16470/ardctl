from setuptools import setup, find_packages

setup(
    name="ardctl",
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
            "ard-remove-apps=app.ard_remove_apps:main",
            "ard-open=app.ard_open:main",
            "ard-align=app.ard_align:main",
            "ard-swipe=app.ard_swipe:main",
        ],
    },
    python_requires=">=3.6",
)
