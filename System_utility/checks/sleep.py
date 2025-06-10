import platform
import subprocess

def check_sleep_settings():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            result = subprocess.run(["powercfg", "/query"], capture_output=True, text=True)
            return "ok" if "10" in result.stdout else "too_high"
        elif os_name == "Darwin":
            result = subprocess.run(["pmset", "-g"], capture_output=True, text=True)
            return "ok" if "sleep 10" in result.stdout else "too_high"
        elif os_name == "Linux":
            result = subprocess.run(["gsettings", "get", "org.gnome.settings-daemon.plugins.power", "sleep-inactive-ac-timeout"], capture_output=True, text=True)
            return "ok" if result.stdout.strip().isdigit() and int(result.stdout.strip()) <= 600 else "too_high"
    except Exception:
        return "unknown"
