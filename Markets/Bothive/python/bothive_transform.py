from ETC import format_json
from Modules.common import *
import pandas as pd

def transformation(dic_bothive, save=False):
    """
    dic_bothive를 수요업체측의 양식인 json_bothive로 맞추는 함수
    :param dic_bothive:
    :return:
    """
    json_bothive = {}
    for dic_key, dic_value in dic_bothive.items():
        json_bothive[dic_key] = format_json.format_json(dic_key)
        json_bothive[dic_key]['name'] = dic_bothive[dic_key]['product'][0]
        json_bothive[dic_key]['brand'] = dic_bothive[dic_key]['brand'][0]
        json_bothive[dic_key]['type'] = dic_bothive[dic_key]['type'][0]
        json_bothive[dic_key]['thumbnail'] = dic_bothive[dic_key]['image'][0]
        json_bothive[dic_key]['summary'][0] = dic_bothive[dic_key]['highlight']
        try:
            json_bothive[dic_key]['warranty']['Servicing (Months)'] = dic_bothive[dic_key]['highlight']['Servicing (Months)']
        except:
            pass
        json_bothive[dic_key]['description'][0] = dic_bothive[dic_key]['description']
        try:
            json_bothive[dic_key]['related_doc_url_1'] = dic_bothive[dic_key]['related']
        except:
            pass
        try:
            json_bothive[dic_key]['dimension'] = dic_bothive[dic_key]['spec']
        except:
            pass

        str_match = {}
        for Str in dic_value['delivery']:
            if 'Price' in Str:
                try:
                    str_match[dic_key] = [Str]
                except Exception as e:
                    print(e)

        for i in str_match.keys():
            json_bothive[dic_key]['price']['original'] = str_match[i][0]

    if save:
        df_bothive = pd.DataFrame(json_bothive).transpose()
        df_bothive.to_csv('../save/json/bothive.csv')
        json_save('../save/json/bothive_result__.json', json_bothive)

    return json_bothive
