from Modules.common import *
from ETC.format_json import format_json
import pandas as pd



def transform(dic_cobot, save=False):
    json_cobot = {}

    for dic_key, dic_value in dic_cobot.items():
        json_cobot[dic_key] = format_json()
        json_cobot[dic_key]['thumbnail'] = dic_cobot[dic_key]['thumbnail']
        json_cobot[dic_key]['name'] = dic_cobot[dic_key]['name']
        json_cobot[dic_key]['summary'] = dic_cobot[dic_key]['summary']
        json_cobot[dic_key]['model_name'] = dic_cobot[dic_key]['model_name']
        json_cobot[dic_key]['options'] = dic_cobot[dic_key]['options']
        json_cobot[dic_key]['description'] = dic_cobot[dic_key]['description']
        # json_cobot[dic_key]['related_doc_url_1'] = dic_cobot[dic_key]['related']
        try:
            json_cobot[dic_key]['dimension'] = dic_cobot[dic_key]['dimension']
        except:
            pass

    if save == True:
        df_cobot = pd.DataFrame(json_cobot).transpose()
        df_cobot.to_csv('../json/cobot.csv')
        json_save('../json/cobot_result_.json', json_cobot)
    return json_cobot

if __name__ == '__main__':
    dic_cobot = json_load('../json/cobot_2depth.json')
    transform(dic_cobot, save=True)