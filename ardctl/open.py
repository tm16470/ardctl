import subprocess
import re

window_size = [
    { "width": 120, "height": 264 },
    { "width": 200, "height": 440 },
    { "width": 280, "height": 616 },
]

def run(args):
    n = 1  # default to mid
    if args.small_screen:
        n = 0
    if args.large_screen:
        n = 2

    window_width = window_size[n]["width"]
    window_height = window_size[n]["height"]

    # adb devices -l
    connected = subprocess.check_output('adb devices -l', shell=True, text=True).split('\n')
    connected = [re.sub(r'[\s]+', ' ', line).strip() for line in connected if line.strip()]
    connected = [line.split(' ') for line in connected if 'device' in line]
    connected = [line for line in connected if line[1] == 'device']

    # running scrcpy detection
    processing = []
    proc = subprocess.check_output(
        'ps -ef | grep "adb -s" | grep "CLASSPATH=/data/local/tmp/scrcpy-server.jar"',
        shell=True, text=True
    ).split('\n')

    for line in proc:
        fields = re.sub(r'\s+', ' ', line.strip()).split(' ')
        if len(fields) > 11 and fields[7] == 'adb' and fields[8] == '-s' and fields[11].startswith('CLASSPATH='):
            processing.append(fields[9])

    # launch scrcpy for each not-running device
    for device in connected:
        serial = device[0]
        if serial not in processing:
            title = f"{device[4][6:]}_{serial[-4:]}" if len(device) >= 5 else serial
            cmd = (
                f'scrcpy -s {serial} '
                '--stay-awake --no-audio '
                '--video-bit-rate 128K --max-fps 15 '
                f'--window-title={title} '
                f'--window-width {window_width} '
                f'--window-height {window_height} &'
            )
            subprocess.run(cmd, shell=True)
