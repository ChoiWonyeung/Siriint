import json
from common import *
from Markets.Daara.python.daara_1depth import crawl_key
from Markets.Daara.python.daara_2depth import crawl_detail
from Markets.Daara.python.daara_transform import trans

def __main__():
    depth1 = crawl_key(save=True, sample=True)
    dic_daara = crawl_detail(depth1, save=True)
    json_daara = trans(dic_daara)

    json_save('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Daara/json/result_daara.json', json_daara)

if __name__ == "__main__":
    __main__()