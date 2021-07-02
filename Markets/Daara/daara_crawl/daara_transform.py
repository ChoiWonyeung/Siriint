import json
from common import *
import daara_configuration.daara_config as config
from ETC import format_json
from daara_postprocess import *

dic_daara = pickle_load(config.path_pickle + 'dic_daara.pkl')
source = pickle_load(config.path_pickle + 'source.pkl')

dic_daara = pp_description1(dic_daara)
dic_daara = pp_description2(dic_daara)
dic_daara = pp_order(dic_daara)
dic_daara = pp_delivery(dic_daara)
dic_daara = pp_seller(dic_daara)


def trans(dic_daara):
    json_daara = {}
    for key, value in dic_daara.items():
        json_daara[key] = format_json.format_json(key)
        json_daara[key]['brand'] = dic_daara[key]['brand'][0]

        try:
            json_daara[key]['description'] = dict(zip(dic_daara[key]['description1'], dic_daara[key]['description2']))
        except Exception as e:
            print(e)

        try:
            json_daara[key]['shipping']['methods'] = dic_daara[key]['delivery'][2]
        except Exception as e:
            print(e)

        try:
            json_daara[key]['name'] = {'{lang}': dic_daara[key]['product'][0]}
        except Exception as e:
            print(e)

        try:
            json_daara[key]['price']['original'] = dic_daara[key]['price'][0]
        except Exception as e:
            print(e)

        try:
            json_daara[key]['summary'] = {'{lang}'+str(j): dic_daara[key]['highlight'][j]
                                          for j in range(len(dic_daara[key]['highlight']))}
        except Exception as e:
            print(e)

        try:
            json_daara[key]['catalogs'] = \
                [{'title': {},
                  'description': {},
                  'image': dic_daara[key]['catalog'][j]} for j in range(len(dic_daara[key]['catalog']))]
        except Exception as e:
            print(e)

    return json_daara

# path = '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Daara/daara_dataResults/'
# with open(path+'daara_json.json', 'w', encoding='utf-8') as file_json:
#     json.dump(json_daara, file_json, indent='\t', ensure_ascii=False)
