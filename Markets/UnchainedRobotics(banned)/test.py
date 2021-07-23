import pickle
from IO import *

with open('pickle/dic_unchained_1depth.pkl', 'rb') as f:
    obj = pickle.load(f)

dic_unchained = pickle_load('pickle/dic_unchained_1depth.pkl')
ls_source = dic_unchained
for post in ls_source:
    print(post)