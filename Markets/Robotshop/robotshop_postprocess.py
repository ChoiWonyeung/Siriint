import pandas as pd
from common import *
from glob import glob
import json

def json_load(file):
    with open(file) as json_file:
        result = json.load(json_file)
        return result

def json2df(file):
    json = json_load(file)
    df = pd.DataFrame(json).transpose()
    result = df.reset_index()
    return result

source = pickle_load('./pickles/source.pkl')


json_ls = glob('./json/*.json')
for i in range(len(json_ls)):
    globals()['df_{}'.format(i)] = json2df(json_ls[i])

df = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9,
                df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17], ignore_index=True)


df = df.drop_duplicates(['index'], keep='last', ignore_index=True)
df2ls = df['index'].tolist()
A = []
for i in source:
    if i not in df2ls:
        A.append(i)

B = []
for j in A:
    B.append(source.index(j))

for i in B:
    print(i)

df1 = df.set_index(['index'])
df2 = df1.transpose()
df3 = df2.to_dict()
json_save('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/robotshop_2depth.json', df3)
pickle_save('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/robotshop.pkl', df3)
df.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/robotshop.csv')
# for a, b in zip(source, df['index']):
#     if a != b:
#         print(source.index(a))
#
# df.isnull().sum()
# len(df4)
# 2001+371
# source.index(df8['index'][289])