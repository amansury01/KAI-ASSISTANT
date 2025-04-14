import psutil

DISTRACTING_APPS = ["chrome", "firefox", "edge", "vlc", "spotify", "netflix", "instagram", "discord", "steam", "youtube"]

def detect_distractions():
    distracting_found = []
    for process in psutil.process_iter(['name']):
        try:
            name = process.info['name'].lower()
            if any(app in name for app in DISTRACTING_APPS):
                distracting_found.append(name)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return distracting_found
