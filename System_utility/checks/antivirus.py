import platform
import subprocess

def check_antivirus():
    os_name = platform.system()

    try:
        if os_name == "Windows":
            import wmi
            w = wmi.WMI(namespace="root\\SecurityCenter2")
            products = w.AntiVirusProduct()
            if products:
                av_names = [product.displayName for product in products]
                return ", ".join(av_names)
            else:
                return "not_found"

        elif os_name == "Darwin":  # macOS
            result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
            known_av = ["Avast", "Norton", "McAfee", "Bitdefender", "Kaspersky", "Sophos"]
            detected = [av for av in known_av if av.lower() in result.stdout.lower()]
            return ", ".join(detected) if detected else "not_found"

        elif os_name == "Linux":
            # Check ClamAV (common on Linux)
            result = subprocess.run(["systemctl", "is-active", "clamav-daemon"], capture_output=True, text=True)
            if "active" in result.stdout:
                return "ClamAV"
            else:
                # Fallback: search for known AV processes
                result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
                known_av = ["clamav", "avgd", "sav-protect", "f-prot", "comodo", "esets", "bitdefender", "kaspersky"]
                detected = [av for av in known_av if av.lower() in result.stdout.lower()]
                return ", ".join(detected) if detected else "not_found"

    except Exception as e:
        return f"unknown ({str(e)})"

# Example usage
if __name__ == "__main__":
    print("Antivirus:", check_antivirus())
