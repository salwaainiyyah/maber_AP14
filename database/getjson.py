import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(BASE_DIR, "list_user.json")

def get_json():
    if not os.path.exists(JSON):
        with open(JSON, "w") as json_file:
            json.dump({}, json_file)
        return {}
        
    with open(JSON, "r") as json_file:
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            data = {}
    return data
    