import pandas as pd
import numpy
import unicodedata

def ls_normalize(df):
    to_list = df.tolist()
    ls_normalized = [unicodedata.normalize('NFC', str(i)) for i in to_list]
    return ls_normalized


def null_numbers(df):
    result = df.index(df.isnull() == True)
    return result


def df_checknull(df):
    global length
    length = len(df)
    Sep = '===================================='
    word = f'해당 데이터 프레임의 길이는 {length} 입니다.'
    null_count = df.isnull().sum()
    null_ratio = round((length - null_count) * 100 / length, 2)
    print(word)
    print(Sep)
    print('널 갯수')
    print(null_count)
    print(Sep)
    print('비율 (%)')
    print(null_ratio)
    print(Sep)


# 특별 변수 지정
null = numpy.nan

drop_column = ['옵션 정보',
               '보증기간',
               '제품 종류별 스펙',
               '패킹(포장) 정보',
               '자율주행 유무',
               '가반하중(kg)',
               '작업반경(mm)',
               '중량',
               '크기',
               '상품 고시 정보',
               '제품정보1',
               'Unnamed: 0',
               'Unnamed: 0.1',
               'Unnamed: 0.1.1']

# 딕셔너리
dic_column = {'브랜드': 'brand',
          '상품명': 'product',
          '모델명': 'model',
          '관련 상품 이미지': 'image',
          '관련 상품 영상': 'video',
          '상품 스펙 정보': 'spec',
          '수집 소스': 'source',
          '분류': 'type1',
          '종류': 'type2',
          '상품 관련 첨부 파일': 'catalog',
          '배송방법': 'delivery2',
          '배송기간': 'delivery',
          '오더 단위별 조건': 'order',
          '판매가 정보': 'price',
          '판매처': 'seller',
          '상품고시정보': 'highlight',
          '상품소개 상세 내용': 'description1',
          '제품정보2': 'description2',
          '소스 분류': 'source_name'}


dic_sourceName = {'bot-hive': '봇하이브',
                  'cobot': '코봇',
                  'daara': '다아라',
                  'komachine': '코머신',
                  'qviro': '큐비로',
                  'thinkbot': '씽크봇 솔루션즈',
                  'robotshop': '로봇샵'}

# 디렉토리
path_resultDir = r'/Users/kimkangnam/Desktop/데이터 바우처/빅웨이브 로보틱스/data_result/'
path_bothive = path_resultDir + 'bothive/'
path_cobot = path_resultDir + 'cobot/'
path_daara = path_resultDir + 'daara/'
path_qviro = path_resultDir + 'qviro/'
path_robotshop = path_resultDir + 'robotshop/'
path_thinkBotSolutions = path_resultDir + 'thinkBotSolutions/'

# 파일들
file_bothive = path_bothive + 'bothive_v0.0.2.csv'
file_cobot = path_cobot + 'cobot_v0.0.1.csv'
file_daara = path_daara + 'daara_v.0.0.2.csv'
file_qviro = path_qviro + 'qviro_v0.0.1.csv'
file_robotshop1 = path_robotshop + 'robotshop_v0.0.2.csv'
file_robotshop2 = path_robotshop + 'robotshop_v0.0.3.csv'
file_robotshop3 = path_robotshop + 'robotshop_v0.0.4.csv'
file_thinkBotSolutions = '/Users/kimkangnam/Desktop/데이터 바우처/빅웨이브 로보틱스/data_result/thinkBotSolutions/thinkBotSolutions_v0.0.1.csv'

# 원본 csv 불러오기
raw_bothive = pd.read_csv(file_bothive, low_memory=False)
raw_cobot = pd.read_csv(file_cobot, low_memory=False)
raw_daara = pd.read_csv(file_daara, low_memory=False)
raw_qviro = pd.read_csv(file_qviro, low_memory=False)
raw_robotshop1 = pd.read_csv(file_robotshop1, low_memory=False)
raw_robotshop1 = raw_robotshop1[:583]
raw_robotshop2 = pd.read_csv(file_robotshop2, low_memory=False)
raw_robotshop2 = raw_robotshop2[550:5083]
raw_robotshop3 = pd.read_csv(file_robotshop3, low_memory=False)
raw_robotshop3 = raw_robotshop3[5080:]
raw_thinkBotSolutions = pd.read_csv(file_thinkBotSolutions, low_memory=False)
raw_robotshop = pd.concat([raw_robotshop1, raw_robotshop2, raw_robotshop3], ignore_index=True)

# 원본 csv 카피본으로 작업
df_bothive = raw_bothive.copy()
df_cobot = raw_bothive.copy()
df_daara = raw_daara.copy()
df_qviro = raw_qviro.copy()
df_robotshop = raw_robotshop.copy()
df_thinkBotSolutions = raw_thinkBotSolutions.copy()