import pandas as pd
from Modules.common import *


def brand_make():
    brand_xl_pre = pd.read_excel('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/brand_list.xlsx', header=1)
    brand_xl_cut1 = brand_xl_pre[:88].transpose()
    brand_xl = brand_xl_cut1[:4].transpose()
    brand_ls = brand_xl['이름'].tolist()
    brand_ls = sorted(brand_ls)
    return brand_ls


def market_key(brand_ls, file='/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/daara_result.json'):
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


def dictionary_normalize(dic_brand):
    dic_brand['ABB'][1] = 'ABB Robotics UK'
    dic_brand['AUBO'][1] = '아우보'
    dic_brand['BOSTON Dynamics'][1] = 'Boston Dynamics'
    dic_brand['DENSO'][1] = 'DENSO Robotics'
    dic_brand['EPSON'][1] = '엡손'
    dic_brand['EPSON'][2] = 'Epson Robotics'
    dic_brand['FANUC'][1] = '화낙(FANUC)'
    dic_brand['FANUC'][2] = 'FANUC UK'
    dic_brand['FRANKA EMIKA'][1] = 'Franka Emika'
    dic_brand['Kawasaki'][1] = '가와사키 로보틱스'
    dic_brand['KUKA'][1] = '쿠카'
    dic_brand['KUKA'][2] = 'Kuka UK'
    dic_brand['NACHI'][1] = '나치 로보틱스 시스템즈'
    dic_brand['NACHI'][2] = 'Nachi Robotics Systems Inc.'
    dic_brand['OMRON'][1] = 'Omron'
    dic_brand['Panasonic'][1] = '파나소닉'
    dic_brand['Schunk'][1] = 'Schunk Intec Ltd'
    dic_brand['STUDIO3S'][1] = '스튜디오쓰리에스'
    dic_brand['YASKAWA'][1] = '야스카와'
    dic_brand['YASKAWA'][2] = 'Yaskawa Motoman'
    dic_brand['두산로보틱스'][1] = 'Doosan Robotics'
    dic_brand['한화기계'][1] = '한화테크윈'
    dic_brand['한화기계'][2] = 'Hanwha Robotics'
    dic_brand['현대로보틱스'][1] = 'Hyundai Robotics'
    return dic_brand


def dictionary_invert(dic_normalized):
    dic_inverted = dict()
    for key1, inner_dict in dic_normalized.items():
        for value in inner_dict.values():
            dic_inverted[value] = key1
    return dic_inverted


def check_brandIn(dic_raw, dic_inverted):
    key_ls = dic_raw.keys()
    brand_marketDup = [dic_raw[key]['brand'] for key in key_ls]
    brand_market = []
    for i in brand_marketDup:
        if i not in brand_market:
            brand_market.append(i)
    brand_market = sorted(brand_market)
    cnt = 0
    for i in brand_market:
        if i in dic_inverted:
            cnt += 1
            print(i)
    print(f'{cnt}개의 브랜드가 매치됩니다.')

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
    dic_brand, dic_raw = market_key(brand_ls, '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/qviro_result.json')
    dic_brandNormalized = dictionary_normalize(dic_brand)
    dic_brandInverted = dictionary_invert(dic_brandNormalized)
    check_brandIn(dic_raw, dic_brandInverted)
    dic_new = brand_sorting(dic_raw, dic_brandInverted)
    return dic_new


if __name__ == '__main__':
    test = {0:'a',
            1:'b',
            '2':'c',
            '3':'d'}
    for i in test:
        test[int(i)] = test[i]
    # conv = int(test)
    # print(test, conv)

    # dic_new = main()
    # json_save('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/_match_qviro.json', dic_new)


    # brand_ls = brand_make()
    # dic_brand, dic_raw = market_key(brand_ls, '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/komachine_result.json')
    # dic_normalized = dictionary_normalize(dic_brand)
    # dic_brandInverted = dictionary_invert(dic_normalized)

    # key_ls = list(dic_raw.keys())
    # for key in key_ls:
    #     dic_raw[key]['brand'] = 'ABB'

    # brand_dup = [dic_raw[key]['brand'] for key in key_ls]
    # brand = []
    # for i in brand_dup:
    #     if i not in brand:
    #         brand.append(i)
    #
    # brand = sorted(brand)










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