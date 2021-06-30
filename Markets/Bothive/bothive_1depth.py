from common import *
import bothive_config

# Chrome webdriver 설정
soup = sel_bsEncoding(bothive_config.url_product)

# 더보기 버튼 클릭 반복
button_more = driver.find_element_by_css_selector(bothive_config.selector_button)
while button_more.text == 'Show me more products':
    try:
        button_more.click()
        sleep_random(15, 20)  # 서버 부하 방지를 위한 슬립
    except:
        break

# 1depth 크롤링
company = ls_driverText(bothive_config.selector_company)  # 회사명 크롤링
category = ls_driverText(bothive_config.selector_category)  # 카테고리 크롤링
product = ls_driverText(bothive_config.selector_product)  # 제품명 크롤링
source = ls_driverHref(bothive_config.selector_source)  # 소스 크롤링
image = ls_driverSrc(bothive_config.selector_image)  # 이미지 크롤링

df_bothive = df_bigWaveRobotics()

df_bothive['product'] = product
df_bothive['Markets'] = company
df_bothive['category'] = category
df_bothive['source'] = source
df_bothive['image'] = image

# 2depth 크롤링에 필요한 딕셔너리 생성
dic_delivery = {}
dic_highlight = {}
dic_description = {}
dic_spec = {}

# 2depth 크롤링
for url2 in source:
    soup = req_bsEncoding(url2)
    sleep_random()
    try:
        dic_highlight[url2] = textmake(bothive_config.selector_essentials)
        dic_description[url2] = textmake(bothive_config.selector_description)
        dic_highlight[url2] = textmake(bothive_config.selector_highlight)
        dic_delivery[url2] = textmake(bothive_config.selector_delivery)

        df_bothive['delivery'] = df_bothive['source'].map(dic_delivery)
        df_bothive['highlight'] = df_bothive['source'].map(dic_highlight)
        df_bothive['description1'] = df_bothive['source'].map(dic_description)
        df_bothive['spec'] = df_bothive['source'].map(dic_spec)

        df_bothive.to_csv('/Users/kimkangnam/Desktop/bothive_v0.0.1.csv')
    except Exception:
        print('Exception occurred')
        pass
