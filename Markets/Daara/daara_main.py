from daara_crawl.daara_1depth import crawl_key
from daara_crawl.daara_2depth import crawl_detail
from daara_crawl.daara_postprocess import *
from daara_crawl.daara_transform import *
from ETC.format_json import *
import daara_configuration.daara_config as config
import json

def daara_run():
    pass
    # source, product, brand, price = crawl_key()
    # dic_daara = pickle_load(config.path_pickle)
    # # dic_daara = crawl_detail(source, product, brand, price)
    # dic_daara = pp_description1(source, dic_daara)
    # dic_daara = pp_description2(source, dic_daara)
    #
    # json_daara = {}
    # for i in source:
    #     json_daara[i] = format_json()
    #     json_daara[i]['brand'] = dic_daara[i]['brand']
    #
    #    with open(, 'w', encoding='utf-8') as file_json:
    #     json.dump(dic_daara, file_json, indent='\t', ensure_ascii=False)


if __name__ == "__main__":
    daara_run()