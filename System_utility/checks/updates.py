import platform
import subprocess

def check_os_updates():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            # PowerShell script to check available updates
            ps_script = r'''
                    $Session = New-Object -ComObject Microsoft.Update.Session
                    $Searcher = $Session.CreateUpdateSearcher()
                    $Results = $Searcher.Search("IsInstalled=0")
                    $Results.Updates.Count
                    '''
            result = subprocess.run(["powershell", "-Command", ps_script], capture_output=True, text=True)

            if result.returncode != 0:
                return "error"

            update_count = result.stdout.strip()
            if update_count.isdigit() and int(update_count) > 0:
                return "updates_available"
            else:
                return "up_to_date"

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
