import json
import os
path = os.path.join('.','user.json')
f = file(path)
j = json.load(f)
f.close()

##j['user']['name'] = u'liming'
##s = json.dumps(j)
##f = file(os.path.join(path,'user3.json'),'w')
##f.write(s)
##f.close()
def get_json_from_file(path):
    f = file(path)
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

def is_register(user_name,uers_json):
    users = uers_json['users']
    for user in users:
        if user['name'] == user_name:
            return True
    return False

def add_user(user_name,user_json,path):
    users = user_json['users']
    users.append(dict(name=user_name))
    write_to_file(json.dumps(user_json),path)

def register(user_name):
    path = os.path.join('.','user.json')
    users_info = get_json_from_file(path)
    if not is_register(user_name,users_info):
        add_user(user_name,users_info,path)
        return True
    return False
