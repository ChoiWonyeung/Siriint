from pprint import pprint
import pandas as pd
import csv

with open('./bigwave_brand.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        brand_ls = row


if 'dic_brand' not in globals():
    dic_brand = {}

# with open('./bigwave_brand.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(brand_ls)






# def dic_write(string, print=False):
#     inner_keys = list(['ABB'].values())
#     inner_len = len(inner_keys)
#     dic_abb['ABB'][str(inner_len)] = string
#     if print:
#         pprint(dic_abb)
#     return dic_abb