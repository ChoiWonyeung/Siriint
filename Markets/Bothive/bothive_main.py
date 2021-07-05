from Markets.Bothive.bothive_crawl.bothive_1depth import crawl_key
from Markets.Bothive.bothive_crawl.bothive_2depth import crawl_detail
from Markets.Bothive.bothive_crawl.bothive_postprocess import postProcess
from Markets.Bothive.bothive_crawl.bothive_transform import *
import json

path = '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Bothive/bothive_dataResults'

def bothive_run():
    brand, type1, product, source, image = crawl_key()
    dic_bothive = crawl_detail(brand, type1, product, source, image)
    dic_bothive = postProcess(dic_bothive)
    json_bothive = trans(dic_bothive)

    with open(path+'json_bothive.json', 'w', encoding='utf-8') as file_json:
        json.dump(json_bothive, file_json, indent='\t', ensure_ascii=False)

    return(json_bothive)


if __name__ == '__main__':
    bothive_run()