from Modules.common import *
import robotshop_config

# def crawl_key():
# webdriver 불러오기
driver = get_webdriver(path_webdriver)


dic_robotshop = {}
sel_bsEncoding('https://www.robotshop.com/en/products.html')
sleep_random(2, 4)
div_menu = driver.find_elements_by_css_selector('div.main-container')
menu_ls = div_menu[0].find_elements_by_css_selector('div.section li a')
menu = [i.get_attribute('href') for i in menu_ls]

sample_menu = menu[0]
source = []
# 제품 소스 긁기
for url in sample_menu:
    sel_bsEncoding(url)
    sleep_random(2, 4)
    div_content = driver.find_elements_by_css_selector('div.category-products')
    source_ls = div_content[0].find_elements_by_css_selector('div.thumbnailCatTop > a')
    for i in source_ls:
        if i.get_attribute('href') not in source:
            source.append(i.get_attribute('href'))

    sample_source = source[:3]

    # 페이지 긁기
    div_page = driver.find_elements_by_css_selector('ol.pagination')
    page_ls = div_page[0].find_elements_by_css_selector('li > a')
    page = []
    for i in page_ls:
        if i.get_attribute('href') not in page:
            page.append(i.get_attribute('href'))

    # 페이지 돌며 소스 긁기'
    for url1 in page:
        sel_bsEncoding(url1)
        sleep_random(2, 4)
        div_content = driver.find_elements_by_css_selector('div.category-products')
        source_ls = div_content[0].find_elements_by_css_selector('div.thumbnailCatTop > a')
        for i in source_ls:
            if i.get_attribute('href') not in source:
                source.append(i.get_attribute('href'))



#
#
# dic_robotshop= {}
# # source 수집 (key)
# cnt = 0
# page = 1
# except_num = 1
#
# while cnt <= 5:
#     print(f'{page}페이지 수집중...')
#     # soup = req_bsEncoding((robotshop_config.dic_url[cnt] + str(page)))
#     soup = req_bsEncoding()
#
#     soup.select('category-products')
#
#     sleep_random(2, 10, print_time=True)
#     dic_robotshop[url] += ls_driverHref(robotshop_config.selector_source)
#     print('--------------------------------------------------------')
#
#     if ls_driverHref(robotshop_config.selector_source) != []:  # 페이지에서 수집 요소가 없을경우
#         page += 1
#     else:
#         print(f'Except occurred : {except_num}')
#         except_num += 1
#         cnt += 1
#         page = 1
#
# # 2차 크롤링
#
# dic_robotshop = {}
# for url2 in source:
#     dic_robotshop[url2] = dic_bigWaveRobotics()
#     sel_bsEncoding(url2)
#     sleep_random(print_time=True)
#
#     for key in robotshop_config.dic_selector.keys():
#         if key == 'image':
#             try:
#                 dic_robotshop[url2][key] = ls_driverFinder(robotshop_config.dic_selector[key], 'data-src')
#             except Exception as e0:
#                 print('Error occurred', key, e0)
#                 pass
#
#         elif key == 'catalog':
#             try:
#                 dic_robotshop[url2][key] = ls_driverHref(robotshop_config.dic_selector[key])
#             except Exception as e1:
#                 print('Error occurred', key, e1)
#                 pass
#
#         else:
#             try:
#                 dic_robotshop[url2][key] = driverText(robotshop_config.dic_selector[key])
#             except Exception as e2:
#                 print('Error occurred', key, e2)
#                 pass
#
# pickle_save('dic_robotshop.pkl', dic_robotshop)