import pickle
import json

def pickle_save(file, obj):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)

def pickle_load(file):
    with open(file, 'rb') as f:
        obj = pickle.load(f)
        return obj

def json_save(file, obj):
    with open(file, 'w') as f:
        json.dump(obj, f)

def json_load(file):
    with open(file, 'r') as f:
        obj = json.load(f)
        return  obj
