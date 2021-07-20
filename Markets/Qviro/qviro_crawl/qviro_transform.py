from common import *
from ETC import format_json
import pandas as pd

def transformation(dic_qviro, save=False):
    json_qviro = {}
    for dic_key, dic_value in dic_qviro.items():
        json_qviro[dic_key] = format_json.format_json()
        json_qviro[dic_key]['type'] = dic_qviro[dic_key]['type']
        json_qviro[dic_key]['brand'] = dic_qviro[dic_key]['brand']
        json_qviro[dic_key]['name'] = dic_qviro[dic_key]['product']
        json_qviro[dic_key]['thumbnail'] = dic_qviro[dic_key]['thumbnail']
        json_qviro[dic_key]['related_doc_url_3'] = dic_qviro[dic_key]['description_img']
        json_qviro[dic_key]['description'] = dic_qviro[dic_key]['description']
        json_qviro[dic_key]['dimension'] = dic_qviro[dic_key]['spec']
        try:
            json_qviro[dic_key]['related_doc_url_4'] = dic_qviro[dic_key]['usecase_video']
            json_qviro[dic_key]['related_doc_url_5'] = dic_qviro[dic_key]['usecase_text']
        except:
            pass
    if save == True:
        df_qviro = pd.DataFrame(json_qviro).transpose()
        df_qviro.to_csv('../json/qviro.csv')
        json_save('../json/qviro_result.json', json_qviro)
    return json_qviro

if __name__ == '__main__':
    dic_qviro = json_load('../json/qviro_2depth.json')
    transformation(dic_qviro, save=True)
