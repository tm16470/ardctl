import subprocess

class ArdCtl:
    def open(self):
        subprocess.run(["scrcpy"])

    def close(self):
        print("未実装: close コマンド")

if __name__ == "__main__":
    import fire
    fire.Fire(ArdCtl)
