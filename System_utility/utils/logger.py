import json
from datetime import datetime

def log(message, level="INFO"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "message": message
    }
    print(json.dumps(log_entry))
