import platform
import subprocess

def check_os_updates():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            result = subprocess.run(["powershell", "(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()"], capture_output=True, text=True)
            return "checked" if result.returncode == 0 else "error"
        elif os_name == "Darwin":
            result = subprocess.run(["softwareupdate", "--list"], capture_output=True, text=True)
            return "updates_available" if "*" in result.stdout else "up_to_date"
        elif os_name == "Linux":
            try:
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                result = subprocess.run(["apt-get", "--just-print", "upgrade"], capture_output=True, text=True)
                return "updates_available" if "Inst" in result.stdout else "up_to_date"
            except Exception:
                return "unknown"
    except Exception:
        return "unknown"
