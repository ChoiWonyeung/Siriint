from Markets.Daara.python.config import *
from common import *
from ETC import format_json
import pandas as pd

def transformation(dic_daara, save=False):
    """
    빅웨이브 로보틱스의 양식에 맞추는 함수
    :param dic_daara:
    :return:
    """
    json_daara = {}
    for key, value in dic_daara.items():
        json_daara[key] = format_json.format_json(key)
        json_daara[key]["name"]['{lang}'] = dic_daara[key]["name"]
        json_daara[key]["brand"] = dic_daara[key]["brand"]
        json_daara[key]["price"]['original'] = dic_daara[key]['price']
        try:
            json_daara[key]["description"] = dic_daara[key]["description"]
        except:
            pass
        try:
            json_daara[key]["catalogs"] = dic_daara['catalog']
        except:
            pass
        try:
            json_daara[key]['options'] = dic_daara[key]['option']
        except:
            pass
        json_daara[key]['thumbnail'] = dic_daara[key]['image']
        json_daara[key]['type'] = dic_daara[key]['category']
        json_daara[key]['summary'] = dic_daara[key]['highlight']
        try:
            json_daara[key]['related_doc_url_1'] = dic_daara[key]['판매자 정보']
        except:
            pass

        try:
            json_daara[key]['related_doc_url_2'] = dic_daara[key]['반품·교환안내']
        except:
            pass
        try:
            json_daara[key]["shipping"]["methods"] = dic_daara[key]["배송안내"]
        except:
            pass
        try:
            json_daara[key]["shipping"]["calculation"] = dic_daara[key]["결제 안내"]
        except:
            pass
    if save:
        df_daara = pd.DataFrame(json_daara).transpose()
        df_daara.to_csv('../json/daara.csv')
        json_save('../json/daara_result__.json', json_daara)
    return json_daara

if __name__ == '__main__':
    dic_daara = json_load('../json/daara_2depth_.json')
    transformation(dic_daara, save=True)