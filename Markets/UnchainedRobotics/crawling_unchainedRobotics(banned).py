from common import *
from bs4 import BeautifulSoup
import unicodedata
import time

def get_webdriver(path_webdriver, wait_time = 20):
    driver = webdriver.Chrome(path_webdriver)
    driver.implicitly_wait(wait_time)
    return driver

def req_bsEncoding(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def sel_bsEncoding(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def ls_hrefmake(selector, str_add = ''): #href->리스트 반환 함수
    ls_href = []
    for href_soup in soup.select(selector):
        ls_href.append(str_add + href_soup['href'])
    return ls_href

def ls_textmake(selector, encoding_type = 'NFKD'): #text->리스트 반환 함수
    ls_text = []
    for text_soup in soup.select(selector):
        ls_text.append(unicodedata.normalize(encoding_type, text_soup.text))
    return ls_text

def ls_textmake2(selector):
    ls_text = []
    for text_soup in soup.select(selector):
        ls_text.append(text_soup.text)
    return ls_text

def check_ip():
    url = 'http://icanhazip.com/'
    res = requests.get(url)
    print(res)
    print(res.text)

def check_response(url):
    res = requests.get(url)
    print(res)

url = 'https://unchainedrobotics.de/en/marketplace/'
sel_bsEncoding(url)

# soup = sel_bsEncoding(url)

#
# # 셀렉터 설정
# selector_product = '.woocommerce-loop-product__title'
selector_category = '.elementor-widget-container'
selector_source = 'h5.jet-woo-product-title > a'
# selector_nextPage = '.next.page-numbers'
#
# # 리스트 만들기
# product = []
category = []
#페이지 소스 긁기
source = ls_hrefmake(selector_source)
#
for i in source[:5]:
    req_bsEncoding(i)
    time.sleep(2)
    category += ls_textmake2(selector_category)

# # 데이터 프레임 컬럼 설정
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
# # 데이터 프레임 생성
# df_cobot = pd.DataFrame(columns = df_columns)
# df_cobot['상품명'] = product
# df_cobot['분류'] = category
# df_cobot['수집 소스'] = source
#
# #
# productMeta = []
# description = []
# selector_productMeta = '.product_meta'
# selector_description = 'div.resp-tabs-container'
#
# dic_addInfo = dict()
#
# for i in df_cobot['수집 소스']:
#     soup = sel_bsEncoding(i)
#     selector_addInfo = '.woocommerce-product-attributes.shop_attributes.table.table-striped'
#     productMeta += ls_textmake2(selector_productMeta)
#     description += ls_textmake2(selector_description)
#     dic_addInfo[i] = ls_textmake2(selector_addInfo)
#
#
# df_cobot['상품고시정보'] = productMeta
# df_cobot['상품소개 상세 내용'] = description
# df_cobot['제품정보1'] = df_cobot['수집 소스']
# df_cobot['제품정보1'] = df_cobot['수집 소스'].map(dic_addInfo)