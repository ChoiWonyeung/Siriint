from common import *
from ETC.format_json import format_json



def transform(dic_cobot):
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

    json_save('./json/cobot_result_.json', json_cobot)
    return json_cobot
