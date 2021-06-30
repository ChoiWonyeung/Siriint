from common import *
import qviro_config

def textmake(selector, normalize_unicode = False, encoding_type = 'NFKD', makeList = True):
    ls = []
    if normalize_unicode == False and makeList == True:
        for text_soup in soup.select(selector):
            ls.append(text_soup.text)
        return ls

    elif normalize_unicode == False and makeList == False:
        for text_soup in soup.select(selector):
            return text_soup.text

    elif normalize_unicode == True and makeList == True:
        for text_soup in soup.select(selector):
            ls.append(unicodedata.normalize(encoding_type, text_soup.text))
        return ls

    elif normalize_unicode == True and makeList == False:
        for text_soup in soup.select(selector):
            return unicodedata.normalize(encoding_type, text_soup.text)


# 1차 크롤링 리스트
product = []
source = []
company = []

# 2차 크롤링 딕셔너리
dic_description = {}
dic_spec = {}
dic_image = {}

# 1차 크롤링 진행 (json 형태)
for page in range(1, 6):
    req = requests.get(qviro_config.url_noNumber + str(page))
    json = req.json()
    length_data: int = (len(json['data']))  # JSON 내부 데이터 길이 측정
    sleep_random()

    # json 에서 데이터 가져오기
    for Number in range(length_data):
        data = json['data'][Number]
        product.append(data['title'])
        company.append(data['Markets'])
        source.append(data['url'])
        sleep_random()

# 데이터 프레임 만들기
df_qviro = df_bigWaveRobotics()
df_qviro['brand'] = company
df_qviro['product'] = product

# 딕셔너리 치환을 위한 키 복사
df_qviro['source'] = source
df_qviro['description1'] = source
df_qviro['spec'] = source
df_qviro['image'] = source

# 2차 크롤링 진행
for url2 in df_qviro['source']:
    soup = sel_bsEncoding(url2)
    sleep_random()

    try:
        # 수집
        dic_description[url2] = textmake(qviro_config.selector_description, normalize_unicode=True, makeList=False)
        dic_spec[url2] = textmake(qviro_config.selector_spec, makeList=False)
        dic_image[url2] = ls_driverSrc(qviro_config.selector_image)
        # 구성
        df_qviro['description1'] = df_qviro['source'].map(dic_description)
        df_qviro['spec'] = df_qviro['source'].map(dic_spec)
        df_qviro['image'] = df_qviro['source'].map(dic_image)

        # 데이터 저장
        df_qviro.to_csv('/Users/kimkangnam/Desktop/quivro_v0.0.2.csv', encoding='utf-8')

    except Exception:
        print('Exception occurred')
        pass
