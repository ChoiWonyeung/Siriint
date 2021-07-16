from common import *
import Markets.Cobot.crawl.cobot_config as config


def crawl_key(save=False, sample=False):
    """

    :param save:
    :param sample:
    :return:
    """
    if sample == True:
        dic_cobot = {}
        soup = req_bsEncoding('https://www.cobotwebshop.com/en/shop/')
        product_things1 = soup.select('ul.products.products-container')
        try:
            product_things2 = product_things1[0].select('li> div > div > a')  # 이름 수정 요망

            for i in product_things2:
                dic_cobot[i['href']] = {}
        except Exception as e:
            print('Exception occurred')

    else:
        # cobot url 설정
        soup = req_bsEncoding(config.url_main)  # request
        sleep_random(2, 4, print_time=True)

        # 메뉴 url 가져오기
        div_menu = soup.select(config.selector_menu)
        menu = div_menu[0].select('li > a')
        url_menu = [i['href'] for i in menu]

        # 메뉴 -> 페이지 순으로 돌아가며 크롤링
        pages = []
        dic_cobot = {}
        for url1 in url_menu:
            url_page = []
            soup = req_bsEncoding(url1)
            sleep_random(2, 4, print_time=True)

            # 제품 리스트 받아오기
            product_things1 = soup.select('ul.products.products-container')
            try:
                product_things2 = product_things1[0].select('li> div > div > a')  # 이름 수정 요망

                for i in product_things2:
                    dic_cobot[i['href']] = {}
            except Exception as e:
                print('Exception occurred')

            # 다음 페이지 정보 받아오기
            try:
                ul_page = soup.select('ul.page-numbers')
                page = ul_page[0].select('li > a')
                for i in page:
                    if i['href'] not in url_page:
                        pages.append(i['href'])
            except:
                pass

            for url2 in pages:
                soup = req_bsEncoding(url2)
                sleep_random(2, 4, print_time=True)

                product_things1 = soup.select('ul.products.products-container')
                try:
                    product_things2 = product_things1[0].select('li> div > div > a')  # 이름 수정 요망

                    for i in product_things2:
                        dic_cobot[i['href']] = {}
                except Exception:
                    print('Exception occurred')

    if save == True:
        json_save('./json/cobot_1depth.json', dic_cobot)
        pickle_save('./pickles/dic_cobot_1depth.pkl', dic_cobot)
    return dic_cobot
