import platform
import subprocess

def check_disk_encryption():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            result = subprocess.run(["manage-bde", "-status", "C:"], capture_output=True, text=True)
            return "enabled" if "Percentage Encrypted: 100%" in result.stdout else "disabled"
        elif os_name == "Darwin":
            result = subprocess.run(["fdesetup", "status"], capture_output=True, text=True)
            return "enabled" if "FileVault is On." in result.stdout else "disabled"
        elif os_name == "Linux":
            result = subprocess.run(["lsblk", "-o", "NAME,FSTYPE"], capture_output=True, text=True)
            return "enabled" if "crypto_LUKS" in result.stdout else "disabled"
    except Exception:
        return "unknown"
