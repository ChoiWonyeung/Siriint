from Modules.common import *
import komachine_config as config


def crawl_key(sample=False, save=False):
    # 1차 크롤링 리스트
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
    if save == True:
        json_save('./json/komachine_1depth.json', dic_komachine)
    pickle_save('./pickles/komachine_1depth.pkl', dic_komachine)
    return dic_komachine

# soup = req_bsEncoding('https://www.komachine.com/ko/companies/abb/products/')
# div_product = soup.select('section.company-products a.item.product')
