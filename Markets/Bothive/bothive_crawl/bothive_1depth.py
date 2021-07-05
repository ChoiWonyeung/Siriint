from common import *
import Markets.Bothive.bothive_configuration.bothive_config as config

def crawl_key():
    # Chrome webdriver 설정
    driver = get_webdriver(path_webdriver)

    # bothive 사이트 불러오기
    sel_bsEncoding(config.url_product)

    # 더보기 버튼 클릭 반복
    button_more = driver.find_element_by_css_selector(config.selector_button)
    # while button_more.text == 'Show me more products':
    #     try:
    #         button_more.click()
    #         sleep_random(15, 20)  # 서버 부하 방지를 위한 슬립
    #     except:
    #         break

    # 1depth 크롤링
    brand = driverText(config.selector_brand)  # 회사명 크롤링
    type1 = driverText(config.selector_type1)  # 카테고리 크롤링
    product = driverText(config.selector_product)  # 제품명 크롤링
    source = ls_driverHref(config.selector_source)  # 소스 크롤링
    image = ls_driverSrc(config.selector_image)  # 이미지 크롤링
    return brand, type1, product, source, image
