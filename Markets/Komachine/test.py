from Modules.common import *
import komachine_config as config


sample = True

source = []
dic_komachine = {}

# 1차 크롤링 [url]
page = 1
while True:
    soup = req_bsEncoding(config.url_fa + str(page))
    sleep_random(2, 4, print_time=True)  # 2 ~ 4초 사이의 float 초만큼 랜덤 sleep
    source += ls_hrefmake(soup, config.selector_source, 'https://www.komachine.com')
    page += 1
    if sample == True:
        break
    else:
        if soup.select(config.selector_source) == []:
            break

soup = req_bsEncoding(config.url_robot)
sleep_random(2, 4, print_time=True)
source_ls = soup.select('div.wrapper > a')
source += ['https://www.komachine.com' + i['href'] for i in source_ls]

for key in source:
    dic_komachine[key] = {}

for dic_key, value in dic_komachine.items():
    print(f"{source.index(dic_key)}번째 반복문 실행중...")
    soup = req_bsEncoding(dic_key)
    sleep_random(print_time=True)

    div_product_info = soup.select('section.product-info')
    # image
    try:
        image_ls = div_product_info[0].select('div.slide img')
        image1 = [i['src'] for i in image_ls]
        image = {}
        for idx, v in enumerate(image1):
            image[idx] = v
        dic_komachine[dic_key]['image'] = image
    except:
        pass

    try:
        video_ls = div_product_info[0].select('div.slide iframe')
        video1 = [i['src'] for i in video_ls]
        video = {}
        for idx, v in enumerate(video1):
            video[idx] = v
        dic_komachine[dic_key]['video'] = video

    except:
        pass

    # product name
    try:
        table = div_product_info[0].select('div.product-doc table tr')

        # product
        product = table[0].select('td')
        dic_komachine[dic_key]['product'] = product[0].text.strip()

        # model
        model = table[1].select('td')
        dic_komachine[dic_key]['model'] = model[0].text.strip()

        # type
        type = table[2].select('td')
        dic_komachine[dic_key]['type'] = type[0].text.strip()

        # catalog
        catalog = {}
        catalog_ls = table[3].select('td a')
        catalog1 = [i['href'] for i in catalog_ls]
        for idx, v in enumerate(catalog1):
            catalog[idx] = v
        dic_komachine[dic_key]['catalog'] = catalog
    except:
        pass

    # description
    try:
        section_description = soup.select('section.product-desc')
        description_ls = section_description[0].select('p')
        description_image1 = section_description[0].select('p img')
        description_text1 = [i.text.strip() for i in description_ls]
        description_text2 = [i.replace('\n', '') for i in description_text1]
        description_text = list(filter(None, description_text2))
        description_image = []

        for i in description_image1:
            try:
                description_image.append(i['href'])
            except:
                description_image.append(i['src'])
        ls_description = description_image + description_text
        description = {}
        for idx, v in enumerate(ls_description):
            description[idx] = v
        dic_komachine[dic_key]['description'] = description

        # product description_add
        div_product_tabs = section_description[0].select('div.product-detail-tab > a')
        div_product_tabs_contents = section_description[0].select('div.product-detail-tab-contents img')

        description_tab = {}
        product_tab = [i.text for i in div_product_tabs]
        product_tab_contents = [i['href'] for i in div_product_tabs_contents]
        for tab, contents in zip(product_tab, product_tab_contents):
            description_tab[tab] = contents
        dic_komachine[dic_key]['description']['tab'] = description_tab

    except Exception as e:
        print(e)
        pass