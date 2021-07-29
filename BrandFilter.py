import pandas as pd
from Modules.common import *
from glob import glob
import re


def string_normalize(input_word):
    return re_specialCharacters(input_word.strip().lower())


def re_specialCharacters(text, eliminate_space=True):
    if eliminate_space:
        result_text = re.sub(r'[^a-zA-Z0-9가-힣]', '', text)
    elif not eliminate_space:
        result_text = re.sub(r'[^a-zA-Z0-9가-힣\s]', '', text)
    return result_text


def make_brand_by_excel():
    brand_xl_pre = pd.read_excel('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/brand_list.xlsx', header=1)
    brand_xl_cut1 = brand_xl_pre[:88].transpose()
    brand_xl = brand_xl_cut1[:4].transpose()
    brand_ls = brand_xl['이름'].tolist()
    brand_ls = sorted(brand_ls)
    return brand_ls


def make_brand():
    dic_brand = {}
    with open('./brand/brand_list.txt', 'r') as f:
        while True:
            line = f.readline()
            if line:
                line_split = line.split(',')
                line_split_strip = [word.strip() for word in line_split]
                line_split_strip_lower = [word.lower() for word in line_split_strip]
                line_re = [re_specialCharacters(word, eliminate_space=True) for word in line_split_strip_lower]
                line_duplicate = tuple(sorted(filter(None, set(line_re))))

                brand_key = line_duplicate
                brand_name_as_value = line_split_strip[0]
                dic_brand[brand_key] = brand_name_as_value
            else:
                break
    return dic_brand


def make_all_market_data():
    file_ls = glob('./makeExcel(full_length)/*_result.json')
    dic_all_markets = {}
    for file in file_ls:
        file_loaded = json_load(file)
        file_key = sorted(list(file_loaded.keys()))
        for k in file_key:
            dic_all_markets[k] = file_loaded[k]
    return dic_all_markets


def count_brand_match(dic_all_markets, dic_brand):
    keys = dic_all_markets.keys()
    cnt = 0
    temps = set()
    for i in keys:
        brand = dic_all_markets[i]['brand']
        for brand_set in dic_brand.keys():
            if string_normalize(brand) in brand_set:
                cnt += 1
                temps.add(dic_brand[brand_set])
    result = sorted(list(temps))
    print(result)
    print(f'{len(result)}개의 브랜드가 매치됩니다.')


def brand_filtering(dic_all_markets, dic_brand):
    dic_filter_by_brand = {}
    for K in dic_all_markets.keys():
        # K는 URL 키
        # 브랜드를 cleansing 처리 하여 할당
        brand = string_normalize(dic_all_markets[K]['brand'])
        # dic_brand 의 키는 cleansing 된 set형 자료
        for brand_set in dic_brand.keys():
            if brand in brand_set:
                dic_filter_by_brand[K] = dic_all_markets[K]
                dic_filter_by_brand[K]['brand'] = dic_brand[brand_set]
    return dic_filter_by_brand


def make_excel(dic_filter_by_brand, filename):
    df = pd.DataFrame(dic_filter_by_brand).transpose()
    brand_list = sorted(list(set(df['brand'].tolist())))

    for i in brand_list:
        if not os.path.exists(
                f'/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/{filename}.xlsx'):
            with pd.ExcelWriter(
                    f'/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/{filename}.xlsx',
                    mode='w', engine='openpyxl') as writer:
                df[df['brand'] == i].to_excel(writer, index=True, sheet_name=i)
        else:
            with pd.ExcelWriter(
                    f'/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/{filename}.xlsx',
                    mode='a', engine='openpyxl') as writer:
                df[df['brand'] == i].to_excel(writer, index=True, sheet_name=i)


def main():
    dic_brand = make_brand()
    dic_all_markets = make_all_market_data()
    dic_filter_by_brand = brand_filtering(dic_all_markets, dic_brand)
    # make_excel(dic_filter_by_brand, 'test')
    count_brand_match(dic_all_markets, dic_brand)
    return dic_filter_by_brand, dic_brand


if __name__ == '__main__':

    dic_filter_by_brand, dic_brand = main()

    # json_save('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/__allResults.json', dic_new)
    # df.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/__allResults.csv')