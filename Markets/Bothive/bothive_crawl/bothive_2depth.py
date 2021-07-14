from common import *
import Markets.Bothive.bothive_configuration.bothive_config as config


def crawl_detail(dic_bothive, save=False):
    driver = get_webdriver(path_webdriver)
    cnt = 1
    # 2depth 크롤링
    for key_dict, value in dic_bothive.items():
        soup = sel_bsEncoding(key_dict)
        sleep_random(print_time=True)
        print(f'{cnt}번째 반복문 실행중...')
        print('--------------------------------')

        # highlight 긁기
        dic_bothive[key_dict]['highlight'] = {}
        top_highlight = soup.select('div.tab__content__body__info')
        highlights = top_highlight[0].select('div p')
        highlight = [high.text for high in highlights]
        head_highlight = []
        body_highlight = []
        for idx, dic_value in enumerate(highlight):
            if idx % 2 == 0:
                head_highlight.append(dic_value)
            elif idx % 2 == 1:
                body_highlight.append(dic_value)
        dic_highlight = dict(zip(head_highlight, body_highlight))
        dic_bothive[key_dict]['highlight'] = dic_highlight

        try:
            dic_bothive[key_dict]['description'] = textmake(soup, config.selector_description)
        except Exception as e:
            print(e)

        specs = soup.select('.tab__key-info__info')
        key_stats = specs[0].select('p')
        dic_bothive[key_dict]['spec'] = {}
        for i in key_stats:
            dic_bothive[key_dict]['spec'][i.text.split(':')[0]] = ''
            dic_bothive[key_dict]['spec'][i.text.split(':')[0]] = i.text.split(':')[1]


        try:
            dic_bothive[key_dict]['delivery'] = textmake(soup, config.selector_delivery)
        except Exception as e:
            print(e)

        # related url
        div_related = driver.find_elements_by_css_selector('div.related__product--wrapper')
        related_ls = div_related[0].find_elements_by_css_selector('.related__product > a')
        related = [i.get_attribute('href') for i in related_ls]
        dic_bothive[key_dict]['related'] = {}
        for idx, v in enumerate(related):
            dic_bothive[key_dict]['related'][idx] = v

        cnt += 1
    if save == True:
        pickle_save('./pickles/bothive_2depth.pkl', dic_bothive)
        json_save('./json/bothive_2depth.json', dic_bothive)
    return dic_bothive

if __name__ == '__main__':
    pass