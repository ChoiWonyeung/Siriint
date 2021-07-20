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
for num, key in enumerate(source[4970:5000]):
    print(f'{source.index(key)}번째 모험')
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

    if num % 10 == 0:
        json_save('json/robotshop_4970_5000.json', dic_robotshop)

json_save('json/robotshop_4970_5000.json', dic_robotshop)

