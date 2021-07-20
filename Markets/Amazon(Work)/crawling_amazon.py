from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import unicodedata

# Chrome webdriver 설정
refer = pd.read_csv('/Users/kimkangnam/Desktop/BWR_데이터 수집 대상 및 항목/시트3. 로봇 및 부품 업체 리스트-표 1.csv')
brand_list = list(refer['이름'])

def return_webdriverSetting(path_webdriver = ''):
    driver = webdriver.Chrome(path_webdriver)
    return driver

def return_bsEncoding(url, time = 20):
    driver.implicitly_wait(time)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def ls_textmake(selector, encoding_type = 'NFKD'): #text->리스트 반환 함수
    ls_text = []
    for text_soup in soup.select(selector):
        ls_text.append(unicodedata.normalize(encoding_type, text_soup.text))
    return ls_text

def ls_hrefmake(selector, str_add = ''): #href->리스트 반환 함수
    ls_href = []
    for href_soup in soup.select(selector):
        ls_href.append(str_add + href_soup['href'])
    return ls_href

def ls_driverText(selector):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.text for element in elements]
    return result

def ls_driverHref(selector):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.get_attribute('href') for element in elements]
    return result

# Chrome webdriver 설정
driver = webdriver.Chrome('/Users/kimkangnam/Desktop/Chromedriver/chromedriver')
soup = return_bsEncoding('https://www.amazon.com/-/ko/s?k=robot&i=toys-and-games&rh=n%3A343404011&dc&language=ko&qid=1623631085&rnid=2941120011&ref=sr_pg_1')

#selector 설정
selector_product = '.a-size-base-plus.a-color-base.a-text-normal'
selector_priceUnit = '.a-price-symbol'
selector_priceSymbol = '.a-price-whole'
selector_priceFraction = '.a-price-fraction'
selector_source = '.a-link-normal.s-no-outline'

# 1depth 크롤링
product = ls_textmake(selector_product)
price_unit = ls_textmake(selector_priceUnit)
price_symbol = ls_textmake(selector_priceSymbol)
price_fraction = ls_textmake(selector_priceFraction)
source = ls_hrefmake(selector_source)

# 데이터 프레임화 및 csv저장
#
# df_columns = ['No',
#               '브랜드',
#               '상품명',
#               '모델명',
#               '관련 상품 이미지',
#               '관련 상품 영상',
#               '상품 관련 첨부 파일',
#               '옵션 정보',
#               '판매가 정보',
#               '보증기간',
#               '배송방법',
#               '배송기간',
#               '제품 종류별 스펙',
#               '상품 스펙 정보',
#               '패킹(포장) 정보',
#               '오더 단위별 조건',
#               '판매처',
#               '상품고시정보',
#               '상품소개 상세 내용',
#               '수집 소스',
#               '소스 분류',
#               '분류',
#               '자율주행 유무',
#               '가반하중(kg)',
#               '작업반경(mm)',
#               '종류',
#               '중량',
#               '크기',
#               '제품정보1',
#               '제품정보2']
#
# df_bothive = pd.DataFrame(columns = df_columns)
# df_bothive['상품명'] = product
# df_bothive['브랜드'] = Markets
# df_bothive['분류'] = category
# df_bothive['수집 소스'] = source
#
# df_bothive.to_csv('/Users/kimkangnam/Desktop/bothive.csv')
