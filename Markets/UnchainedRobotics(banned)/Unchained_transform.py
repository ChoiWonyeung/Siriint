from IO import *
from ETC import format_json
import pandas as pd


def transformation(dic_unchained, save=False):
    json_unchained ={}
    num = 1
    for key, value in dic_unchained.items():

        json_unchained[key] = format_json.format_json(key)
        json_unchained[key]["type"] = 'tangible'
        try:json_unchained[key]["name"] = dic_unchained[key]["Product"]
        except:pass
        try:json_unchained[key]["summary"] = dic_unchained[key]['Information']
        except:pass
        try:json_unchained[key]["brand"] = dic_unchained[key]["Brand"]
        except:pass
        try:json_unchained[key]['vendor'] = dic_unchained[key]['Seller']
        except:pass
        try:json_unchained[key]["price"]['original'] = dic_unchained[key]["Price"]
        except:pass
        json_unchained[key]["thumbnail"] = str(dic_unchained[key]["Image"]).replace('[','').replace(']','').replace('"','').replace("'","")

        json_unchained[key]["catalogs"] = dic_unchained[key]['Description']

        try:json_unchained[key]["model_name"] = dic_unchained[key]["Model"]
        except:pass

        try:json_unchained[key]["related_doc_url_1"] = dic_unchained[key]["File"]
        except:pass
        print(str(len(dic_unchained.items()))+" "+str(num))
        num= num+1
        print(json_unchained[key])

    if save == True:
        df_unchained = pd.DataFrame(json_unchained).transpose()
        df_unchained.to_csv('data/unchained_result.csv')
        json_save('data/unchained_result.json', json_unchained)

if __name__ == '__main__':
    dic_unchained = json_load('data/unchained.json')
    transformation(dic_unchained, save=True)