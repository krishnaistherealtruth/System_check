import winreg
import platform
import subprocess
import getpass
import os

def check_login():
    os_name = platform.system()

    try:
        if os_name == "Windows":
            reg_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
            autologon = winreg.QueryValueEx(key, "AutoAdminLogon")
            if (autologon != "1"):
                return "Auto Login"
            else:
                return "Password Login"

        elif os_name == "Darwin":
            username = getpass.getuser()
            result = subprocess.run(["dscl", ".", "-authonly", username],
                                    input=b"\n",
                                    stdout=subprocess.PIDE,
                                    stderr=subprocess.PIDE)
            if result.returncode == 0:
                return "Password login"
            else:
                return "No Password login"

        elif os_name == "Linux":
            ssh_config_path = "/etc/ssh/sshd_config"
            if not os.path.exists(ssh_config_path):
                return "SSH config not found"

            with open(ssh_config_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("PasswordAuthentication"):
                        value = line.split()[1].lower()
                        if value == "yes":
                            return "Password Login"
                        elif value == "no":
                            return "No Password Login"
            # If not explicitly set, default is usually "yes"
            return "Password Login"

    except:
        return "Unknown"


