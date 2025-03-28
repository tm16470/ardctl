from setuptools import setup, find_packages

setup(
    name="android-ctrl",
    version="0.1.0",
    description="A CLI tool to manage Android screens and apps",
    packages=find_packages(),
    install_requires=[
        "fire"
    ],
    entry_points={
        "console_scripts": [
            "remove-default-apps=app.remove_default_apps:main",
            "open-screens=app.open_screens:main",
            "swipe-screens=app.swipe_screens:main",
        ],
    },
    python_requires=">=3.6",
)
