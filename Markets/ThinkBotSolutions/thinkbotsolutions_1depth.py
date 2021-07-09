from common import *
import thinkbotsolutions_config_backup

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


def ls_srcmake(selector, str_add=''):
    ls_src = []
    for src_soup in soup.select(selector):
        ls_src.append(str_add + src_soup['src'])
    return ls_src


# 1차 크롤링 리스트
company = []
product = []
price = []
source = []

# 2차 크롤링 딕셔너리
dic_image = dict()
dic_sku = dict()
dic_description = dict()
dic_specifications = dict()
dic_video = dict()

# 1차 크롤링 범위
range_actual = range(1, 5)
range_sample = range(1, 3)

# 1차 크롤링 시행
for page in range_actual:
    soup = req_bsEncoding(thinkbotsolutions_config_backup.url_noNumber + str(page))
    sleep_random()

    product += textmake(thinkbotsolutions_config_backup.selector_product)
    company += textmake(thinkbotsolutions_config_backup.selector_company)
    price += textmake(thinkbotsolutions_config_backup.selector_price)
    source += ls_hrefmake(thinkbotsolutions_config_backup.selector_source, 'https://thinkbotsolutions.com/')

# 데이터 프레임화 및 csv저장
df_thinkBotSolutions = df_bigWaveRobotics()
df_thinkBotSolutions['product'] = product
df_thinkBotSolutions['brand'] = company
df_thinkBotSolutions['price'] = price
df_thinkBotSolutions['source'] = source

for i in df_thinkBotSolutions['source']:
    soup = req_bsEncoding(i)
    sleep_random()

    try:
        dic_sku[i] = textmake(thinkbotsolutions_config_backup.selector_sku)
        dic_description[i] = textmake(thinkbotsolutions_config_backup.selector_description)
        dic_specifications[i] = textmake(thinkbotsolutions_config_backup.selector_specifications)
        dic_video[i] = ls_srcmake(thinkbotsolutions_config_backup.selector_video)
        dic_image[i] = ls_srcmake(thinkbotsolutions_config_backup.selector_image)

        df_thinkBotSolutions['description1'] = df_thinkBotSolutions['source'].map(dic_description)
        df_thinkBotSolutions['spec'] = df_thinkBotSolutions['source'].map(dic_specifications)
        df_thinkBotSolutions['model'] = df_thinkBotSolutions['source'].map(dic_sku)
        df_thinkBotSolutions['video'] = df_thinkBotSolutions['source'].map(dic_video)

        df_thinkBotSolutions.to_csv('/Users/kimkangnam/Desktop/thinkBotSolutions_v0.0.1.csv')
    except Exception:
        print('Exception occured')
        pass
