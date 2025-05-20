from .disk import check_disk_encryption
from .updates import check_os_updates
from .antivirus import check_antivirus
from .sleep import check_sleep_settings

def perform_all_checks():
    return {
        "disk_encryption": check_disk_encryption(),
        "os_update_status": check_os_updates(),
        "antivirus_status": check_antivirus(),
        "sleep_setting_status": check_sleep_settings()
    }
