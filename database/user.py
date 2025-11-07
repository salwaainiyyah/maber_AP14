import json
import os

import bcrypt

from database.getjson import get_json
from ui_utils import error, success

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(BASE_DIR, "list_user.json")

def check_user(username, password):
    data = get_json()

    if username in data:
        stored_hashed = data[username]["password"]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed.encode('utf-8')):
            success("Login berhasil!")
            return True
        else:
            error("Password salah!")
            return 
    else:
        error("Pengguna tidak ditemukan!")
        return 

def create_user(username, password):
    data = get_json()

    if username in data:
        error("Pengguna sudah ada!")
        return 
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        data[username] = {
            "username": username,
            "password": hashed_password.decode('utf-8'),
            "total_level": 0,
            "title": "bronze"
        }
        with open(JSON, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
        
        
def update_user(username, level, title):
    data = get_json()

    if (username in data):
        new_data = {
        "username": username,
        "total_level": level,
        "title": title
    }
        data[username] = new_data  
        with open(JSON, "w") as json_file:
            json.dump(data, json_file)