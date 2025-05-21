import subprocess

class ArdCtl:
    def open(self):
        subprocess.run(["scrcpy"])

if __name__ == "__main__":
    import fire
    fire.Fire(ArdCtl())
