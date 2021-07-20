import Markets.Bothive.configuration.bothive_config as config
from Modules.common import *

# Chrome webdriver 설정
driver = get_webdriver(path_webdriver, headless=True)

# bothive 사이트 불러오기
sel_getPageSource(driver, config.url_product)
sample = True
# 더보기 버튼 클릭 반복
button_more = driver.find_elements_by_css_selector('div.products-gallery__wrapper.block-spacing')
button = button_more[0].find_elements_by_css_selector('button')
button[3].text

try:
    button_more.click()
    sleep_random(15, 20, print_time=True)  # 서버 부하 방지를 위한 슬립
except:
    pass

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
    dic_bothive[url2]['Information'] = [type1[idx]]
    dic_bothive[url2]['Image'] = [image[idx]]
save = False
if save == True:
    pickle_save('/Markets/save/pickles/dic_json.pkl', dic_bothive)
    json_save('/Markets/Bothive/save/json/bothive_1depth.json', dic_bothive)