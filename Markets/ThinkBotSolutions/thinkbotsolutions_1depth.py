import common
from bs4 import BeautifulSoup
from selenium import webdriver
import thinksolutions_config as config


# common.json_save()

url_page = 'https://thinkbotsolutions.com/collections/all?page='

def crawl_key(make_breakpoint=False, save=False, sample=False):
    result = {}
    # 크롤링 1page ~ 마지막 페이지 (1depth)
    page = 1
    while True:
        print(f"{page}페이지 수집중...")
        url = f"{url_page}{page}"
        soup = common.req_bsEncoding(url)
        common.sleep_random(print_time=True)
        div_list = soup.select('div.product-item.product-item--vertical')
        for div in div_list:
            a = div.select("a")[0]
            href = a['href']
            key = f"https://thinkbotsolutions.com/{href}"
            result[key] = {}

            result[key]['brand'] = div.select("div.product-item__info-inner a")[0].text
            result[key]['name'] = div.select("div.product-item__info-inner a")[1].text

            try:
                price_one = div.select("div.product-item__price-list.price-list span")[0].text
                if price_one.split(' '):
                    result[key]['price'] = price_one.split(' ')[1]
            except:
                result[key]['price'] = {}

        if div_list == [] or sample == True:
            print("크롤링이 곧 종료됩니다.")
            break
        else:
            page += 1
            if make_breakpoint is True:
                breakpoint()  # 테스트를 위한 break point


    if save == True:
        common.json_save('./json/1depth.json', result)
    return result

# if __name__ == '__main__':
#     dic_thinkbotsolutions = crawl_key(sample=True, save=True)