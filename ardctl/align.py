import pywinctl

def run(args=None):
    screens = pywinctl.getAllWindowsDict().get('scrcpy', {}).get('windows', {})
    if not screens:
        print("No scrcpy windows found.")
        return

    position = get_position(screens)
    titles = list(screens.keys())

    for i, title in enumerate(titles):
        wins = pywinctl.getWindowsWithTitle(title)
        if wins:
            wins[0].moveTo(position[i][0], position[i][1])

def get_position(screens):
    position = []
    first_key = next(iter(screens))
    window_size = screens[first_key]["size"]
    x, y = 0, 0

    for i in range(len(screens)):
        if i == 0:
            pass
        elif i == 1:
            y = window_size.height + 37
        else:
            if i % 2 == 0:
                x += window_size.width
                y = 0
            else:
                y = window_size.height + 37
        position.append([x, y])
    return position
