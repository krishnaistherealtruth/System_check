import requests
from utils.logger import log

def report_to_server(data, retries=3):
    for i in range(retries):
        try:
            response = requests.post("http://127.0.0.1:8000/report", json=data, timeout=10)
            if response.status_code == 200:
                return True
        except requests.RequestException as e:
            log(f"Attempt {i+1} failed: {e}", level="WARNING")
    return False
