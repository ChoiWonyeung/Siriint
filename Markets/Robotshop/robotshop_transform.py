from common import *
from ETC import format_json
import pandas as pd

def transformation(dic_robotshop, save=False):
    json_robotshop = {}
    for dic_key, dic_value in dic_robotshop.items():
        json_robotshop[dic_key] = format_json.format_json()
        json_robotshop[dic_key]['thumbnail'] = dic_robotshop[dic_key]['image']
        json_robotshop[dic_key]['type'] = dic_robotshop[dic_key]['category']
        json_robotshop[dic_key]['name'] = dic_robotshop[dic_key]['product']
        json_robotshop[dic_key]['price'] = dic_robotshop[dic_key]['price']
        json_robotshop[dic_key]['summary'] = dic_robotshop[dic_key]['highlight']
        json_robotshop[dic_key]['model_name'] = {dic_robotshop[dic_key]['model']}
        json_robotshop[dic_key]['description'] = dic_robotshop[dic_key]['description']
        json_robotshop[dic_key]['dimension'] = dic_robotshop[dic_key]['spec']
        json_robotshop[dic_key]['related_doc_url_1'] = dic_robotshop[dic_key]['related']

    if save == True:
        df_robotshop = pd.DataFrame(json_robotshop).transpose()
        df_robotshop.to_csv('./json/robotshop_result.csv')
        json_save('./json/robotshop_result.json', json_robotshop)
    return json_robotshop

if __name__ == '__main__':
    dic_robotshop = pickle_load('./pickles/robotshop.pkl')
    transformation(dic_robotshop, save=True)
