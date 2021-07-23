from Pickle import *
from ETC import format_json
import pandas as pd


def transformation(dic_amazon, save=False):

    json_amazon ={}

    for key, value in dic_amazon.item():
        json_amazon[key] = format_json.format_json(key)
        try:json_amazon[key]["name"] = {'{lang}':dic_amazon[key]["Product"]}
        except:pass
        try:json_amazon[key]["summary"] = {'{lang}':dic_amazon[key]["Information"]}
        except:pass
        try:json_amazon[key]["brand"] = dic_amazon[key]["Brand"]
        except:pass
        try:json_amazon[key]['vendor'] = dic_amazon[key]['Seller']
        except:pass
        try:json_amazon[key]["price"]['original'] = dic_amazon[key]["Price"]
        except:pass
        json_amazon[key]["thumbnail"] = dic_amazon[key]["Image"]
        json_amazon[key]["shipping"] = dic_amazon[key]["Shipping"]
        json_amazon[key]["catalogs"] = dic_amazon[key]['Description']
        try:json_amazon[key]["option"] = dic_amazon[key]["Option"]
        except:pass
        try:json_amazon[key]["model_name"] = dic_amazon[key]["Model"]
        except:pass
        try:json_amazon[key]["dimension"] = dic_amazon[key]["Specification"]
        except:pass
    if save == True:
        df_amazon = pd.DataFrame(json_amazon).transpose()
        df_amazon.to_csv('data/amazon_result.csv')
        json_save('data/amazon_result.json', json_amazon)

if __name__ == '__main__':
    dic_amazon = json_load('data/amazon.json')
    transformation(dic_amazon, save=True)