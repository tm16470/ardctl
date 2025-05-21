import subprocess

class ArdCtl:
    def open(self):
        subprocess.run(["scrcpy"])

def main():
    import fire
    fire.Fire(ArdCtl())

if __name__ == "__main__":
    main()

