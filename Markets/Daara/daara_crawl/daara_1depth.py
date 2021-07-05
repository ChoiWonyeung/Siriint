from common import *
import daara_configuration.daara_config as config


def crawl_key(make_breakpoint=False):
    """
    마켓플레이스의 상품 리스트에서 Key로 이용하는 source(url)을 수집하는 함수.
    Key 제외 1 depth 포함 수집 항목
    product = 상품명, brand = 브랜드, price = 가격
    :return:
    """
    # 크롤링 1page ~ 마지막 페이지 (1depth)
    product = []
    brand = []
    price = []
    source = []
    page = 1
    while True:
        print(f'{page}페이지 수집중...')
        soup = req_bsEncoding(config.url_page + str(page))
        sleep_random(print_time=True)

        key = ls_hrefmake(soup, config.selector_source)
        source += ls_hrefmake(soup, config.selector_source, 'http://mall.daara.co.kr/product/')
        brand += textmake(soup, config.selector_brand)
        price += textmake(soup, config.selector_price)
        product += textmake(soup, config.selector_product)
        print('---------------------------------------------')
        if key == []:
            print('크롤링이 곧 종료됩니다.')
            break
        else:
            break
            page += 1
            if make_breakpoint is True:
                breakpoint()   # 테스트를 위한 break point
    return source, product, brand, price
