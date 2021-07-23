import pandas as pd
from Modules.common import *


def brand_make():
    brand_xl_pre = pd.read_excel('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/brand_list.xlsx', header=1)
    brand_xl_cut1 = brand_xl_pre[:88].transpose()
    brand_xl = brand_xl_cut1[:4].transpose()
    brand_ls = brand_xl['이름'].tolist()
    return brand_ls


def market_key(brand_ls, file='/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/daara_result__.json'):
    dic_raw = json_load(file)
    ls_marketKey = list(dic_raw.keys())

    a = []
    for key in ls_marketKey:
         a.append(dic_raw[key]['brand'])

    dic_brand = {}
    for i in sorted(brand_ls):
        dic_brand[i] = {}
        dic_brand[i][0] = i
    return dic_brand, dic_raw


def dictionary_normalize(dic):
    dic['YASKAWA'][1] = '야스카와'
    dic['AUBO'][1] = '아우보'
    dic['Panasonic'][1] = '파나소닉'
    dic['EPSON'][1] = '엡손'
    dic['NACHI'][1] = '나치 로보틱스 시스템즈'
    dic['Kawasaki'][1] = '가와사키 로보틱스'
    dic['한화기계'][1] = '한화테크윈'
    dic['STUDIO3S'][1] = '스튜디오쓰리에스'
    dic['FANUC'][1] = '화낙(FANUC)'
    dic['KUKA'][1] = '쿠카'
    return dic


def dictionary_invert(dic_normalized):
    dic_inverted = dict()
    for key1, inner_dict in dic_normalized.items():
        for value in inner_dict.values():
            dic_inverted[value] = key1
    return dic_inverted


def brand_sorting(dic_raw, dic_brandInverted):
    dic_new = {}
    for key in list(dic_raw.keys()):
        if dic_raw[key]['brand'] in dic_brandInverted.keys():
            brand = dic_raw[key]['brand']
            dic_new[key] = dic_raw[key]
            dic_new[key]['brand'] = dic_brandInverted[brand]
    return dic_new


def main():
    brand_ls = brand_make()
    dic_brand, dic_raw = market_key(brand_ls)
    dic_brandNormalized = dictionary_normalize(dic_brand)
    dic_brandInverted = dictionary_invert(dic_brandNormalized)
    dic_new = brand_sorting(dic_raw, dic_brandInverted)
    return dic_new


if __name__ == '__main__':
    dic_new = main()





        # goal이 안쪽 딕셔너리의 value로 존재하면



    #     if goal in inner_dict.values():
    #         # temp dict에 key를 goal로 해서 inner dict를 복사
    #         temp_dict[goal] = inner_dict
    #     else:
    #         # 존재하지 않으면 기존키 (key1) 유지
    #         temp_dict[key1] = inner_dict
    #
    # # 새로운 딕셔너리로 덮어쓰기
    # dic_normalized = temp_dict
    # for key in delete_keys:
    #     del dic_normalized[key]

    # for i in dic.values():
    #     print(i.values())
    # for key in daara_raw.keys():
    #     if daara_raw[key]['brand'] in