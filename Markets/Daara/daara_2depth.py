import daara_config
from common import *


def key_crawling():
    # 크롤링 1page ~ 마지막 페이지 (1depth)
    product = []
    brand = []
    price = []
    source = []
    cnt = 0
    page = 1
    while cnt == 0:
        print(f'{page}페이지 수집중...')
        soup = req_bsEncoding(daara_config.url_page + str(page))
        sleep_random(print_time=True)

        source += ls_hrefmake(daara_config.selector_source, 'http://mall.daara.co.kr/product/')
        brand += textmake(daara_config.selector_brand)
        price += textmake(daara_config.selector_price)
        product += textmake(daara_config.selector_product)
        print('---------------------------------------------')
        if ls_hrefmake(daara_config.selector_source) == []:
            cnt += 1
            print('크롤링이 곧 종료됩니다.')
        else:
            page += 1
        break
    return source, product, brand, price

def detail_crawling(source, product, brand, price):
    dic_daara = {}
    page_num = 1
    for url2 in source:
        dic_daara[url2] = dic_bigWaveRobotics(url2)
        dic_daara[url2]['product'] = product[source.index(url2)]
        dic_daara[url2]['brand'] = brand[source.index(url2)]
        dic_daara[url2]['price'] = price[source.index(url2)]

        print(f'{page_num}번째 반복문 실행중...')
        page_num += 1
        soup = req_bsEncoding(url2)
        sleep_random(print_time=True)

        for key in daara_config.dic_selector.keys():
            if key == 'catalog':
                try:
                    dic_daara[url2][key] = ls_hrefmake(daara_config.dic_selector[key])
                except Exception as e1:
                    print('Error occurred', key, e1)
                    pass

            elif key == 'image':
                try:
                    dic_daara[url2][key] = ls_srcmake(daara_config.dic_selector[key])
                except Exception as e2:
                    print('Error occurred', key, e2)
                    pass

            else:
                try:
                    dic_daara[url2][key] = textmake(daara_config.dic_selector[key])
                except Exception as e3:
                    print('Error occurred', key, e3)
                    pass
    return dic_daara

if __name__ == "__main__":
    source, product, brand, price = key_crawling()
    dic_daara = detail_crawling(source, product, brand, price)
    pickle_save('dic_daara.plk', dic_daara)
