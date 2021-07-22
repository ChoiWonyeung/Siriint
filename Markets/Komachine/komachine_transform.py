from Modules.common import *
from ETC import format_json
import pandas as pd

def transformation(dic_komachine, save=False):
    """
    빅웨이브 로보틱스의 양식에 맞추는 함수
    :param dic_daara:
    :return:
    """
    dic_komachine = json_load('./json/komachine_2depth.json')

    json_komachine = {}
    for key, value in dic_komachine.items():
        json_komachine[key] = format_json.format_json(key)
        json_komachine[key]["name"]['{lang}'] = dic_komachine[key]["product"]
        json_komachine[key]["model"] = dic_komachine[key]["model"]
        json_komachine[key]['type'] = dic_komachine[key]['type']
        json_komachine[key]['thumbnail'] = dic_komachine[key]['image']['0']
        json_komachine[key]['catalogs'] = dic_komachine[key]['catalog']

        # description
        description = {}
        a = dic_komachine[key]['description_text']
        b = dic_komachine[key]['description_image']
        c = a + b
        for idx, v in enumerate(c):
            description[idx] = v
        json_komachine[key]['description'] = description

    if save == True:
        df_komachine = pd.DataFrame(json_komachine).transpose()
        df_komachine.to_csv('./json/komachine.csv')
        json_save('./json/komachine_result__.json', json_komachine)
    return json_komachine

if __name__ == '__main__':
    dic_komachine = json_load('./json/komachine_2depth.json')
    transformation(dic_komachine, save=True)