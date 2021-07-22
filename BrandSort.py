from glob import glob
import pandas as pd
from Modules.common import *


def brand_make():
    brand_xl_pre = pd.read_excel('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/brand_list.xlsx', header=1)
    brand_xl_cut1 = brand_xl_pre[:88].transpose()
    brand_xl = brand_xl_cut1[:4].transpose()
    brand_ls = brand_xl['이름'].tolist()
    return brand_ls

def daara_key(brand_ls):
    daara_raw = json_load('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/daara_result__.json')
    daara_keylist = list(daara_raw.keys())
    # for brand in brand_ls:
    #     globals()['brandDic_{}'.format(brand)] = {}

    a = []
    for key in daara_keylist:
         a.append(daara_raw[key]['brand'])

    # b = []
    # for i in a:
    #     if i not in brand_ls:
    #         b.append(i)

    dic = {}
    for i in sorted(brand_ls):
        dic[i] = {}
        dic[i][0] = i
    return dic, daara_raw

def normalize(dic):
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

if __name__ == '__main__':
    from pprint import pprint
    brand_ls = brand_make()
    dic, daara_raw = daara_key(brand_ls)
    dic_normalized = normalize(dic)

    i = list(daara_raw.keys())[0]

    pprint(dic_normalized)
    goal = '아우보'

    delete_keys = []
    temp_dict = dict()
    for key1, inner_dict in dic_normalized.items():
        # goal이 안쪽 딕셔너리의 value로 존재하면
        if goal in inner_dict.values():
            # temp dict에 key를 goal로 해서 inner dict를 복사
            temp_dict[goal] = inner_dict
        else:
            # 존재하지 않으면 기존키 (key1) 유지
            temp_dict[key1] = inner_dict

    # 새로운 딕셔너리로 덮어쓰기
    dic_normalized = temp_dict
    for key in delete_keys:
        del dic_normalized[key]

    pprint(dic_normalized)

    # for i in dic.values():
    #     print(i.values())
    # for key in daara_raw.keys():
    #     if daara_raw[key]['brand'] in