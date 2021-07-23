import pickle
import json

def pickle_save(file, obj):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)

def pickle_load(file):
    with open(file, 'rb') as f:
        obj = pickle.load(f)
        return obj

def json_save(file, object):
    with open(file, 'w', encoding='utf-8') as file_json:
        json.dump(object, file_json, indent='\t', ensure_ascii=False)

def json_load(file):
    with open(file, 'r', encoding='utf-8') as f:
        obj = json.load(f)
        return  obj
