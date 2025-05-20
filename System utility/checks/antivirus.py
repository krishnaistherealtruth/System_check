import platform
import subprocess

def check_antivirus():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            import wmi
            w = wmi.WMI(namespace="root\\SecurityCenter2")
            products = w.AntiVirusProduct()
            return "enabled" if products else "not_found"
        elif os_name == "Darwin":
            result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
            if "Avast" in result.stdout or "Norton" in result.stdout:
                return "enabled"
            return "not_found"
        elif os_name == "Linux":
            result = subprocess.run(["systemctl", "is-active", "clamav-daemon"], capture_output=True, text=True)
            return "enabled" if "active" in result.stdout else "not_found"
    except Exception:
        return "unknown"
