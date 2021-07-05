import daara_configuration.daara_config as config
from common import *

def crawl_detail(source, product, brand, price):
    """
    다아라 수집 값의 dictionary(hash)를 만드는 함수.
    source(url, key)를 반복하여 접속하여 수집 항목에 따라 dictionary 구성
    정제 단계에서 모든 dictionary는 list 형태로 구성
    :param source:
    :param product:
    :param brand:
    :param price:
    :return:
    """
    dic_daara = {}
    cnt = 1
    for url2 in source:
        idx = source.index(url2)
        dic_daara[url2] = dic_bigWaveRobotics(url2)
        dic_daara[url2]['product'] = [product[idx]]
        dic_daara[url2]['brand'] = [brand[idx]]
        dic_daara[url2]['price'] = [price[idx]]

        print(f'{cnt}번째 반복문 실행중...')
        print('--------------------------------')
        cnt += 1
        soup = req_bsEncoding(url2)
        sleep_random(print_time=True)  # 무작위 n초동안 슬립 (default : 2 ~ 10)

        for key_dict in config.dic_selector.keys():
            if key_dict == 'catalog':
                try:
                    dic_daara[url2][key_dict] = ls_hrefmake(soup, config.dic_selector[key_dict])
                except Exception as e1:
                    print('Error occurred\n', key_dict, e1)
                    pass

            elif key_dict == 'image':
                try:
                    dic_daara[url2][key_dict] = ls_srcmake(soup, config.dic_selector[key_dict])
                except Exception as e2:
                    print('Error occurred\n', key_dict, e2)
                    pass

            else:
                try:
                    dic_daara[url2][key_dict] = textmake(soup, config.dic_selector[key_dict])
                except Exception as e3:
                    print('Error occurred\n', key_dict, e3)
                    pass
    return dic_daara

