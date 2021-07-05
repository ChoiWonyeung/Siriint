import json
from daara_crawl.daara_1depth import crawl_key
from daara_crawl.daara_2depth import crawl_detail
from daara_crawl.daara_transform import *

path = '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Daara/daara_dataResults/'

def daara_run():
    source, product, brand, price = crawl_key()
    # dic_daara = pickle_load(config.path_pickle)
    dic_daara = crawl_detail(source, product, brand, price)
    dic_daara = pp_description1(dic_daara)
    dic_daara = pp_description2(dic_daara)
    dic_daara = pp_delivery(dic_daara)
    dic_daara = pp_seller(dic_daara)
    result = trans(dic_daara)
    with open(path+'json_daara.json', 'w', encoding='utf-8') as file_json:
        json.dump(result, file_json, indent='\t', ensure_ascii=False)

    return result


if __name__ == "__main__":
    json_daara = daara_run()
    print(json_daara)