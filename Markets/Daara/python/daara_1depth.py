from common import *
import Markets.Daara.python.config as config

def crawl_key(make_breakpoint=False, save=False, sample=False):
    """
    마켓플레이스의 상품 리스트에서 Key로 이용하는 source(url)을 수집하는 함수.
    Key 제외 1 depth 포함 수집 항목
    product = 상품명, brand = 브랜드, price = 가격
    :return:
    """
    result = {}
    page = 1
    while True:
        print(f"{page}페이지 수집중...")
        url = f"{config.url_page}{page}"
        soup = req_bsEncoding(url)
        sleep_random(print_time=True)
        
        # crawling
        div_list = soup.select(".bbsSubFixed_left_wrap")
        for div in div_list:
            a = div.select("a")[0]
            href = a["href"]
            key = f"http://mall.daara.co.kr/product/{href}"
            result[key] = {}

            # name crawling
            result[key]['name'] = div.select("p.name")[0].text.strip()

            # brand crawling
            result[key]['brand'] = div.select("p.brand")[0].text.strip()

            # price crawling
            result[key]['price'] = div.select("p.btn_estimate.btn_estimate--list")[0].text.strip()

        # 1depth 수집 종료 조건
        if div_list == [] or sample == True:
            print("크롤링이 곧 종료됩니다.")
            break
        else:
            page += 1
            if make_breakpoint is True:
                breakpoint()  # 테스트를 위한 break point

    if save == True:
        json_save(config.path_json + '/1depth.json', result)
    return result

if __name__ == '__main__':
    print(config.path_json + '/1depth.json')