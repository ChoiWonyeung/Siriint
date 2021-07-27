from pprint import pprint

if 'dic_abb' not in globals():
    dic_abb = {}
    dic_abb['ABB'] = {}

def dic_write(string, print=False):
    inner_keys = list(dic_abb['ABB'].values())
    inner_len = len(inner_keys)
    dic_abb['ABB'][str(inner_len)] = string
    if print:
        pprint(dic_abb)
    return dic_abb

dic_write('ABB')
dic_write('abb')
dic_write('에이비비')

pprint(dic_abb)