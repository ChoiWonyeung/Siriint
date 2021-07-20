from common import *

# def crawl_key():
# webdriver 불러오기

driver = get_webdriver(path_webdriver)

dic_robotshop = {}
# source = []
# for page in range(1, 174):
#     sel_getPageSource(driver, f'https://www.robotshop.com/en/robots-to-build.html?p={page}')
#     print(page)
#     source_ls = driver.find_elements_by_css_selector('div.product-name-box > h2 > a')
#     for i in source_ls:
#         source.append(i.get_attribute('href'))
# pickle_save('./pickles/source.pkl', source)

source = pickle_load('./pickles/source.pkl')
source.index('https://www.robotshop.com/en/grove-human-presence-sensor-ak9753.html')
A = [3000, 3982, 3983, 3984, 3985, 3986, 3987, 3988, 3989, 3990, 3991, 3992, 3993, 3994, 3995, 3996, 3997, 3998, 3999, 4966, 4967, 4968, 4969, 5590, 5591, 5592, 5593, 5594, 5595, 5596, 5597, 5598, 5599, 6111, 6112, 6113]
# for num, key in enumerate(source):
for i in A:
    key = source[i]
    # print(f'{source.index(key)}번째 모험')
    sel_getPageSource(driver, key)
    div_type = driver.find_elements_by_css_selector('div.breadcrumbs')
    div_top = driver.find_elements_by_css_selector('div.product-col-box')
    div_bottom = driver.find_elements_by_css_selector('div.product-page-bottom-section')
    dic_robotshop[key] = {}

    # category
    try:
        print('category')
        category1 = div_type[0].find_elements_by_css_selector('li')
        category2 = [i.text.strip() for i in category1]
        category = {}
        for idx, v in enumerate(category2):
            category[idx] = v
        dic_robotshop[key]['category'] = category
    except:
        pass

    # image
    try:
        print('image')
        image_ls = div_top[0].find_elements_by_css_selector('div > img')
        image1 = [i.get_attribute('src') for i in image_ls]
        image = {}
        for idx, v in enumerate(image1):
            image[idx] = v
        dic_robotshop[key]['image'] = image
    except:
        pass

    # product
    try:
        print('product')
        product1 = div_type[0].find_elements_by_css_selector('li.product')
        product = [i.text.strip() for i in product1]
        dic_robotshop[key]['product'] = product[0]
    except:
        pass

        # brand
        # try:
        #     print('brand')
        #     brand1 = driver.find_elements_by_css_selector('brandLogoBox > a')
        #     brand = [i.text.strip() for i in brand1]
        #     dic_robotshop[key]['brand'] = brand[0].text.strip()
        # except:
        #     pass

        # price
        try:
            print('price')
            price1 = div_top[0].find_elements_by_css_selector('span.price')
            price = [i.text for i in price1]
            dic_robotshop[key]['price'] = price
        except:
            pass

        # highlight
        try:
            print('highlight')
            highlight1 = div_top[0].find_elements_by_css_selector('section.product-short-desc > ul > li')
            highlight2 = [i.text.strip() for i in highlight1]
            highlight = {}
            for idx, v in enumerate(highlight2):
                highlight[idx] = v
            dic_robotshop[key]['highlight'] = highlight
        except:
            pass

        # model
        try:
            print('model')
            model1 = driver.find_elements_by_css_selector('h2.product-code-sku strong')
            model = [i.text.strip() for i in model1]
            dic_robotshop[key]['model'] = model[0]
        except:
            pass

        # description
        try:
            print('description')
            description = []
            descriptipon_p = []
            description1 = driver.find_elements_by_css_selector('#description')
            description_ls_p = description1[0].find_elements_by_css_selector('p')
            description_ls_p_img1 = description1[0].find_elements_by_css_selector('p > img')
            description_p_text = [i.text.strip() for i in description_ls_p]
            description_p_img = [i.get_attribute('src') for i in description_ls_p_img1]
            description_ls_li = description1[0].find_elements_by_css_selector('li')
            description_li = [i.text.strip() for i in description_ls_li]

            description.extend(description_p_text)
            description.extend(description_p_img)
            description.extend(description_li)
            description_ = list(filter(None, description))

            dic_robotshop[key]['description'] = description_
        except:
            pass

        # spec
        try:
            print('spec')
            spec1 = driver.find_elements_by_css_selector('#Specifications')
            spec2 = spec1[0].find_elements_by_css_selector('li')
            spec3 = [i.text.strip() for i in spec2]
            spec = {}
            for idx, v in enumerate(spec3):
                spec[idx] = v
                dic_robotshop[key]['spec'] = spec
        except:
            print('no spec')
            pass

        # useful Links
        try:
            print('useful_links')
            related1 = driver.find_elements_by_css_selector('#Useful-Links')
            related2 = related1[0].find_elements_by_css_selector('li > a')
            related3 = [i.get_attribute('href') for i in related2]
            related = {}
            for idx, v in enumerate(related3):
                related[idx] = v
            dic_robotshop[key]['related'] = related
        except:
            pass

        if source.index(key) % 10 == 0:
            json_save('json/robotshop_extra.json', dic_robotshop)

    json_save('json/robotshop_extra.json', dic_robotshop)

















#sample_menu = menu[0]
# source = []
# # # 제품 소스 긁기
# for url in sample_menu:
#     sel_getPageSource(driver, url)
#     sleep_random(2, 4)
#     div_content = driver.find_elements_by_css_selector('div.category-products')
#     source_ls = div_content[0].find_elements_by_css_selector('div.thumbnailCatTop > a')
#     for i in source_ls:
#         if i.get_attribute('href') not in source:
#             source.append(i.get_attribute('href'))
#
#     sample_source = source[:3]
#
#     # 페이지 긁기
#     div_page = driver.find_elements_by_css_selector('ol.pagination')
#     page_ls = div_page[0].find_elements_by_css_selector('li > a')
#     page = []
#     for i in page_ls:
#         if i.get_attribute('href') not in page:
#             page.append(i.get_attribute('href'))
#
#     # 페이지 돌며 소스 긁기'
#     for url1 in page:
#         sel_getPageSource(driver, url1)
#         sleep_random(2, 4)
#         div_content = driver.find_elements_by_css_selector('div.category-products')
#         source_ls = div_content[0].find_elements_by_css_selector('div.thumbnailCatTop > a')
#         for i in source_ls:
#             if i.get_attribute('href') not in source:
#                 source.append(i.get_attribute('href'))














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



# from common import *
# import robotshop_config
#
# # def crawl_key():
# # webdriver 불러오기
# driver = get_webdriver(path_webdriver)
#
#
# dic_robotshop = {}
# sel_getPageSource(driver, 'https://www.robotshop.com/en/products.html')
# sleep_random(2, 4)
# div_menu = driver.find_elements_by_css_selector('div.main-container')
# menu_ls = div_menu[0].find_elements_by_css_selector('div.section li a')
# menu = [i.get_attribute('href') for i in menu_ls]
#
# sample_menu = menu[0]
# source = []
# # 제품 소스 긁기
# for url in sample_menu:
#     sel_getPageSource(driver, url)
#     sleep_random(2, 4)
#     div_content = driver.find_elements_by_css_selector('div.category-products')
#     source_ls = div_content[0].find_elements_by_css_selector('div.thumbnailCatTop > a')
#     for i in source_ls:
#         if i.get_attribute('href') not in source:
#             source.append(i.get_attribute('href'))
#
#     sample_source = source[:3]
#
#     # 페이지 긁기
#     div_page = driver.find_elements_by_css_selector('ol.pagination')
#     page_ls = div_page[0].find_elements_by_css_selector('li > a')
#     page = []
#     for i in page_ls:
#         if i.get_attribute('href') not in page:
#             page.append(i.get_attribute('href'))
#
#     # 페이지 돌며 소스 긁기'
#     for url1 in page:
#         sel_getPageSource(driver, url1)
#         sleep_random(2, 4)
#         div_content = driver.find_elements_by_css_selector('div.category-products')
#         source_ls = div_content[0].find_elements_by_css_selector('div.thumbnailCatTop > a')
#         for i in source_ls:
#             if i.get_attribute('href') not in source:
#                 source.append(i.get_attribute('href'))
#
#
#
# #
# #
# # dic_robotshop= {}
# # # source 수집 (key)
# # cnt = 0
# # page = 1
# # except_num = 1
# #
# # while cnt <= 5:
# #     print(f'{page}페이지 수집중...')
# #     # soup = req_bsEncoding((robotshop_config.dic_url[cnt] + str(page)))
# #     soup = req_bsEncoding()
# #
# #     soup.select('category-products')
# #
# #     sleep_random(2, 10, print_time=True)
# #     dic_robotshop[url] += ls_driverHref(robotshop_config.selector_source)
# #     print('--------------------------------------------------------')
# #
# #     if ls_driverHref(robotshop_config.selector_source) != []:  # 페이지에서 수집 요소가 없을경우
# #         page += 1
# #     else:
# #         print(f'Except occurred : {except_num}')
# #         except_num += 1
# #         cnt += 1
# #         page = 1
# #
# # # 2차 크롤링
# #
# # dic_robotshop = {}
# # for url2 in source:
# #     dic_robotshop[url2] = dic_bigWaveRobotics()
# #     sel_bsEncoding(url2)
# #     sleep_random(print_time=True)
# #
# #     for key in robotshop_config.dic_selector.keys():
# #         if key == 'image':
# #             try:
# #                 dic_robotshop[url2][key] = ls_driverFinder(robotshop_config.dic_selector[key], 'data-src')
# #             except Exception as e0:
# #                 print('Error occurred', key, e0)
# #                 pass
# #
# #         elif key == 'catalog':
# #             try:
# #                 dic_robotshop[url2][key] = ls_driverHref(robotshop_config.dic_selector[key])
# #             except Exception as e1:
# #                 print('Error occurred', key, e1)
# #                 pass
# #
# #         else:
# #             try:
# #                 dic_robotshop[url2][key] = driverText(robotshop_config.dic_selector[key])
# #             except Exception as e2:
# #                 print('Error occurred', key, e2)
# #                 pass
# #
# # pickle_save('dic_robotshop.pkl', dic_robotshop)