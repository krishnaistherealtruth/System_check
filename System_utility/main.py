import uuid
import time
from datetime import datetime,  timezone
import platform
from checks import perform_all_checks
from impor.logger import log
from impor.state import load_last_state, save_state
from impor.reporter import report_to_server
from config import CHECK_INTERVAL_MINUTES

def collect_data():
    return {
        "machine_id": str(uuid.getnode()),
        "platform": platform.system(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **perform_all_checks()
    }

def run_daemon():
    log("Starting System Health Utility daemon...")
    while True:
        log("Performing system checks...")
        current_data = collect_data()
        previous_data = load_last_state()

        if current_data != previous_data:
            log("Change detected and saved. Reporting to server...")
            save_state(current_data)
            if report_to_server(current_data):
                log("Report sent and state saved.")
            else:
                log("Failed to send report.")
        else:
            log("No changes detected.")
        time.sleep(CHECK_INTERVAL_MINUTES * 60)

if __name__ == "__main__":
    run_daemon()
