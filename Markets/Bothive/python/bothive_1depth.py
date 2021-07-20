import Markets.Bothive.configuration.bothive_config as config
from Modules.common import *

# 셀레니움
def crawl_key(save=False, headless=True, sample=False):
    # Chrome webdriver 설정
    driver = get_webdriver(path_webdriver, headless)
    # bothive 사이트 불러오기
    sel_getPageSource(driver, config.url_product)
    sleep_random(2, 5, print_time=True)
    # 더보기 버튼 클릭 반복
    cnt = 0
    while sample==False:
        sleep_random(15, 20, print_time=True)  # 서버 부하 방지를 위한 슬립
        if cnt == 3:
            break
        else:
            button_more = driver.find_elements_by_css_selector('div.products-gallery__wrapper')
            button_ls = button_more[0].find_elements_by_css_selector('button')
            button = [i.text for i in button_ls]

            if 'Show me more products' in button:
                button_idx = button.index('Show me more products')
                button_ls[button_idx].click()
            else:
                cnt += 1
                print(f'시도 횟수 : {cnt}')
                continue

    # 1depth 크롤링
    source = ls_driverHref(driver, config.selector_source)  # 소스 크롤링
    brand = driverText(driver, config.selector_brand)  # 회사명 크롤링
    type1 = driverText(driver, config.selector_type1)  # 카테고리 크롤링
    product = driverText(driver, config.selector_product)  # 제품명 크롤링
    image = ls_driverSrc(driver, config.selector_image)  # 이미지 크롤링

    dic_bothive = {}
    for idx, url2 in enumerate(source):
        dic_bothive[url2] = {}
        dic_bothive[url2]['Product'] = [product[idx]]
        dic_bothive[url2]['Brand'] = [brand[idx]]
        dic_bothive[url2]['type'] = [type1[idx]]
        dic_bothive[url2]['Image'] = [image[idx]]

    if save == True:
        pickle_save('/Markets/save/pickles/dic_json.pkl', dic_bothive)
        json_save('/Markets/Bothive/save/json/bothive_1depth.json', dic_bothive)
    return dic_bothive

