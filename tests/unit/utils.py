import json
import logging
import os
from datetime import datetime
from typing import Optional

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def get_empty_config_file_name():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"config_{timestamp}.json"

def create_config_file(config, filename):
    with open(filename, "w") as file:
        json.dump(config, file, cls=JSONEncoder, indent=4)

def load_config_file(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file, object_hook=lambda d: {k: datetime.fromisoformat(v) if k == "timestamp" else v for k, v in d.items()})
    except json.JSONDecodeError:
        logging.error("Invalid JSON file")
        return None

def get_last_config_file():
    config_files = list(filter(lambda x: x.endswith(".json"), os.listdir()))
    if not config_files:
        return None
    return max(config_files)

def get_latest_config_file_path():
    filename = get_last_config_file()
    return os.path.join(os.path.dirname(__file__), filename) if filename else None