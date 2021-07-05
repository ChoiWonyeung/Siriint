from Markets.Bothive.bothive_crawl.bothive_1depth import crawl_key
from common import *
import Markets.Bothive.bothive_configuration.bothive_config as config


def crawl_detail(brand, type1, product, source, image):
    dic_bothive = {}
    cnt = 1
    for url2 in source:
        idx = source.index(url2)
        dic_bothive[url2] = dic_bigWaveRobotics(url2)
        dic_bothive[url2]['product'] = [product[idx]]
        dic_bothive[url2]['brand'] = [brand[idx]]
        dic_bothive[url2]['type1'] = [type1[idx]]
        dic_bothive[url2]['image'] = [image[idx]]

    print(f'{cnt}번째 반복문 실행중...')
    print('--------------------------------')
    cnt += 1

    # 2depth 크롤링
    for key_dict, value in dic_bothive.items():
        soup = req_bsEncoding(key_dict)
        sleep_random(print_time=True)
        try:
            dic_bothive[key_dict]['highlight'] = textmake(soup, config.selector_highlight)
        except Exception as e:
            print(e)

        try:
            dic_bothive[key_dict]['description1'] = textmake(soup, config.selector_description1)
        except Exception as e:
            print(e)

        try:
            dic_bothive[key_dict]['description2'] = textmake(soup, config.selector_description2)
        except Exception as e:
            print(e)

        try:
            dic_bothive[key_dict]['spec'] = textmake(soup, config.selector_spec)
        except Exception as e:
            print(e)

        try:
            dic_bothive[key_dict]['delivery'] = textmake(soup, config.selector_delivery)
        except Exception as e:
            print(e)
    return dic_bothive

# if __name__ == '__main__':
#         brand, type1, product, source, image = crawl_key()
#         dic_bothive = crawl_detail(brand, type1, product, source, image)
#         pickle_save(config.path_pickle + 'dic_bothive.pkl', dic_bothive)