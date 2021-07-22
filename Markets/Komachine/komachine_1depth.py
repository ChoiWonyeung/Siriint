from Modules.common import *
import komachine_config as config


def crawl_key(sample=False):
    # 1차 크롤링 리스트
    source = []

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
    return source

if __name__ == '__main__':
    source = crawl_key()

# soup = req_bsEncoding('https://www.komachine.com/ko/companies/abb/products/')
# div_product = soup.select('section.company-products a.item.product')
