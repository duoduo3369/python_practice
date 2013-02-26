import json
import os
from django.core.files import locks

path = './javascript/static/data/user.json'
def get_json_from_file(path):
    f = open(path,'r')
    locks.lock(f, locks.LOCK_EX)
    try:
        j = json.load(f)
    finally:
        f.close()
        return j
    
def write_to_file(s,path):
    f = file(path,'w')
    try:
        f.write(s)
    finally:
        f.close()

def register_validation(user_name,uers_json):
    users = uers_json['users']
    for user in users:
        if user['name'] == user_name:
            return True
    return False

def add_user(user_name,user_json,path):
    users = user_json['users']
    users.append(dict(name=user_name))
    write_to_file(json.dumps(user_json),path)

def is_register(user_name):
    global path
    users_info = get_json_from_file(path)
    return register_validation(user_name,users_info)

def register(user_name):
    global path
    users_info = get_json_from_file(path)
    if not register_validation(user_name,users_info):
        add_user(user_name,users_info,path)
        return True
    return False
