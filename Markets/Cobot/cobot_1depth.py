from common import *
import cobot_config


def textmake(selector, normalize_unicode=False, encoding_type='NFKD', makeList=True):
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


def ls_hrefmake(selector, str_add=''):  # href->리스트 반환 함수
    ls_href = []
    for href_soup in soup.select(selector):
        ls_href.append(str_add + href_soup['href'])
    return ls_href


# cobot url 설정
soup = req_bsEncoding(cobot_config.url_main)  # request

# 메뉴 url 가져오기
menu = ls_hrefmake(cobot_config.selector_menu)

# 1차 크롤링 리스트 만들기
product = []
category = []
source = []
# 2차 크롤링 딕셔너리
dic_productMeta = {}
dic_description = {}
dic_image = {}
dic_addInfo = {}

range_actual = range(1, 6)
range_sample = range(1, 3)
for url1 in menu:
    for page_num in range_actual:
        soup = sel_bsEncoding(url1 + 'page/' + str(page_num))
        product += textmake(cobot_config.selector_product)
        category += textmake(cobot_config.selector_category)
        source += ls_hrefmake(cobot_config.selector_source)
        sleep_random()

# 데이터 프레임 생성
df_cobot = df_bigWaveRobotics()
df_cobot['product'] = product
df_cobot['category'] = category
df_cobot['source'] = source

for url2 in df_cobot['source']:
    soup = sel_bsEncoding(url2)
    sleep_random()

    try:
        dic_productMeta[url2] = textmake(cobot_config.selector_productMeta)
        dic_description[url2] = textmake(cobot_config.selector_description)
        dic_addInfo[url2] = textmake(cobot_config.selector_addInfo)
        dic_image[url2] = ls_driverSrc(cobot_config.selector_image)

        df_cobot['highlight'] = df_cobot['source'].map(dic_productMeta)
        df_cobot['description1'] = df_cobot['source'].map(dic_description)
        df_cobot['spec'] = df_cobot['source'].map(dic_addInfo)
        df_cobot['image'] = df_cobot['source'].map(dic_image)

        df_cobot.to_csv('/Users/kimkangnam/Desktop/cobot_v0.0.2.csv')
    except Exception:
        print('Exception occurred')
        pass
