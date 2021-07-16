from Z_Dummy.config_postprocess import *
import numpy
from collections import Counter

# 1단계 : 개별처리
df_daara['상품고시정보'] = df_daara['상품 고시 정보']
df_daara['상품소개 상세 내용'] = df_daara['제품정보1']

# 2단계 : 데이터 합치기
df = pd.concat([df_bothive, df_cobot, df_daara, df_qviro, df_thinkBotSolutions], ignore_index=True)  # 로봇샵 제외
df.rename(columns=dic_column, inplace=True)
df = df.append(df_robotshop, ignore_index=True)  # 로봇샵 합치기
df.drop(drop_column, axis=1, inplace=True)  # 불필요 컬럼 버리기

# 소스(key)로 중복제거
df.drop_duplicates(['source'], keep='first', inplace=True, ignore_index=True)

ls_source = df['source'].tolist()
for i in df:
    print(i)
    for j in ls_source:
        if i != 'source':
            df[i].replace(j, numpy.nan, inplace=True)
        else:
            pass

df.fillna(numpy.nan, inplace=True)

# 중복제거 후 브랜드 리스트
ls_brand = df['brand'].tolist()
ls_brand = set(ls_brand)

# 데이터프레임 전체에 [] 제거
df = df.replace('[]', null)
df['source_name'] = df['source']

for i in range(len(df)):
    for j in dic_sourceName.keys():
        if j in df['source_name'][i]:
            df['source_name'] = df['source_name'].replace(df['source_name'][i], dic_sourceName[j])

# 브랜드 갯수
count_brand = Counter(df['brand'])
ratio_brand = count_brand

for i in ratio_brand.keys():
    ratio_brand[i] = round(ratio_brand[i]/len(df), 2)

No = [i for i in range(1, len(df)+1)]
df['No'] = No

df = df.fillna('')

df['delivery'] = df['delivery'].replace('Price: ', '', regex=True).replace("£££", '', regex=True).replace(r"''", '', regex=True)
df['delivery'] = df['delivery'].replace(r',', '', regex=True)
df['spec'] = df['spec'].replace('Key Stats ', '', regex=True)
df['price'] = df['price'].replace(r'\n', '', regex=True)
df['model'] = df['model'].replace(r"Supplier Product Code\n", '', regex=True)
df = df.replace('', null, regex=True)
df_checknull(df)
df.to_csv(path_resultDir + 'result_v0.0.1.csv')

# df['delivery'] = df['delivery'].replace('Price:', '', regex=True).replace("['']", '', regex=True)

###################################
# TODO 다아라
# 다아라
daara = df[df['source_name'] == '다아라']
# 인덱스 리셋
daara.reset_index(drop=True, inplace=True)

#'\\n'제거
# daara['seller'] = daara['seller'].replace(r'\\n', '', regex=True)
# daara['description1'] = daara['description1'].replace(r'\n', '', regex=True)

# 파싱 daara['seller']
daara_seller = ls_normalize(daara['seller'])
range_seller = range(len(daara_seller))
daara_seller = [daara_seller[i][2:-2] for i in range_seller]
daara_seller = [daara_seller[i].split("\\n") for i in range_seller]
daara_seller = [[j.strip() for j in i] for i in daara_seller]
daara_seller = [list(filter(None, daara_seller[i])) for i in range_seller]
daara_seller2 = []
for i in daara_seller:
    try:
        my_index = i.index('사업장소재지')+1
        daara_seller2.append([i[j] for j in range(0, my_index + 1)])
    except:
        daara_seller2.append(null)
daara['seller'] = daara_seller2

# 파싱 daara['order']
daara_order = ls_normalize(daara['order'])
range_order = range(len(daara_order))
daara_order = [daara_order[i][2:-2] for i in range_order]
daara['order'] = daara_order

# 파싱 daara['description1']
daara_description1 = ls_normalize(daara['description1'])
range_description1 = range(len(daara_description1))
daara_description1 = [daara_description1[i].split('\n') for i in range_description1]
daara_description1 = [list(filter(None, daara_description1[i])) for i in range_description1]
daara_description1 = [daara_description1[i][1:] for i in range_description1]
A = [daara_description1[i][0] for i in range_description1]
A = [A[i].split() for i in range_description1]

A_differ = [len(A[i])-1 for i in range_description1]
for i in range_description1:
    for j in range(A_differ[i]):
        daara_description1[i].insert(j, 'A')

for i in range_description1:
    for j in range(len(A[i])):
        daara_description1[i][j] = A[i][j]
daara['description1'] = daara_description1


# 파싱 daara['description2']
daara_description2 = ls_normalize(daara['description2'])
range_description2 = range(len(daara_description2))
daara_description2 = [daara_description2[i].split('\n') for i in range_description2]
daara_description2 = [[j.strip() for j in i] for i in daara_description2]
daara_description2 = [list(filter(None, daara_description2[i])) for i in range_description2]
daara['description2'] = daara_description2

for i in range(len(daara)):
    if len(daara_description1[i]) == len(daara_description2[i]):
        A.append(i)

# 파싱 daara['catalog']
daara_catalog = ls_normalize(daara['catalog'])
range_catalog = range(len(daara_catalog))
daara_catalog = [daara_catalog[i][2:-2] for i in range_catalog]
daara_catalog = [daara_catalog[i].split(',') for i in range_catalog]
daara_catalog = [list(filter(None, daara_catalog[i]))for i in range_catalog]
daara['catalog'] = daara_catalog

# daara.to_csv(path_daara + 'daara_v1.0.0.csv')