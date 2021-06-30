from common import *
import komachine_config


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


# 1차 크롤링 리스트
product = []  # 상품명
title = []    # 분류
series = []   # 종류
source = []   # 수집소스

# 2차 크롤링 딕셔너리
dic_catalog = {}
dic_description = {}
dic_image = {}

# 1차 크롤링 [상품명, 분류, 종류, 수집소스]
range_actual = range(1, 37)
range_sample = range(1, 3)
for url1 in range_actual:
    soup = req_bsEncoding(komachine_config.url_page + str(url1))
    sleep_random()  # 2 ~ 10초 사이의 float 초만큼 랜덤 sleep

    product += textmake(komachine_config.selector_product)
    title += textmake(komachine_config.selector_title)
    series += textmake(komachine_config.selector_series)
    source += ls_hrefmake(komachine_config.selector_source, 'https://www.komachine.com')
    sleep_random()

df_komachine = df_bigWaveRobotics()
df_komachine['source'] = source
df_komachine['type1'] = title
df_komachine['type2'] = series
df_komachine['product'] = product

# 2차 크롤링
for url2 in df_komachine['source']:
    soup = sel_bsEncoding(url2)
    sleep_random()

    try:
        dic_catalog[url2] = ls_driverHref(komachine_config.selector_catalog)
        dic_description[url2] = ls_driverText(komachine_config.selector_description)
        dic_image[url2] = ls_driverStyle(komachine_config.selector_image)

        df_komachine['catalog'] = df_komachine['source'].map(dic_catalog)
        df_komachine['description1'] = df_komachine['source'].map(dic_description)

        df_komachine.to_csv('/Users/kimkangnam/Desktop/komachine_v0.0.1.csv')
    except Exception:
        print('Exception occurred')
        pass
