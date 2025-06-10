import requests
from impor.logger import log


def report_to_server(data, retries=3):
    log(f"Attempting to send data: {data}", level="INFO")

    for i in range(retries):
        try:
            log(f"Attempt {i + 1}: Sending POST to http://127.0.0.1:8000/report", level="INFO")
            response = requests.post("http://127.0.0.1:8000/report", json=data, timeout=10)

            log(f"Response status code: {response.status_code}", level="INFO")
            log(f"Response content: {response.text}", level="INFO")

            if response.status_code == 200:
                log("Report sent successfully!", level="INFO")
                return True
            else:
                log(f"Server responded with status {response.status_code}: {response.text}", level="WARNING")

        except requests.RequestException as e:
            log(f"Attempt {i + 1} failed: {e}", level="WARNING")

    log("All retry attempts failed", level="ERROR")
    return False