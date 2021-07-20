from Modules.common import *
import Markets.Bothive.configuration.bothive_config as config


def crawl_detail(dic_bothive, save=False, headless=True):
    driver = get_webdriver(path_webdriver, headless)

    # validation
    source_pre0 = pickle_load('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Bothive/save/pickles/bothive_2depth.pkl')
    source_pre = list(source_pre0.keys())
    source0 = pickle_load('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Bothive/save/pickles/bothive_2depth.pkl')
    source = list(source0.keys())
    update = [key for key in source if key not in source_pre]
    if update == []:
        source = source
        print('update 없음')
    elif update != []:
        source = update
        print(f'update {len(update)}개 항목 존재')

    # 2depth 크롤링
    for key_dic in source:
        sel_getPageSource(driver, key_dic)
        sleep_random(print_time=True)
        print(f'{source.index(key_dic)}번 항목 크롤링')
        print('--------------------------------')

        # Information 긁기
        dic_bothive[key_dic]['Information'] = {}
        top_information = driver.find_elements_by_css_selector(config.selector_information)
        informations = top_information[0].find_elements_by_css_selector('div p')
        information = [info.text for info in informations]
        head_information = []
        body_information = []
        for idx, dic_value in enumerate(information):
            if idx % 2 == 0:
                head_information.append(dic_value)
            elif idx % 2 == 1:
                body_information.append(dic_value)
        dic_information = dict(zip(head_information, body_information))
        dic_bothive[key_dic]['Information'] = dic_information

        try:
            dic_bothive[key_dic]['Description'] = driverText(driver, config.selector_description)
        except Exception as e:
            print(e)

        specs = driver.find_elements_by_css_selector(config.selector_spec)
        key_stats = specs[0].find_elements_by_css_selector('p')
        dic_bothive[key_dic]['Spec'] = {}
        for i in key_stats:
            dic_bothive[key_dic]['Spec'][i.text.split(':')[0]] = ''
            dic_bothive[key_dic]['Spec'][i.text.split(':')[0]] = i.text.split(':')[1]

        try:
            dic_bothive[key_dic]['Delivery'] = driverText(driver, config.selector_delivery)
        except Exception as e:
            print(e)

        # related url
        div_related = driver.find_elements_by_css_selector('div.related__product--wrapper')
        related_ls = div_related[0].find_elements_by_css_selector('.related__product > a')
        related = [i.get_attribute('href') for i in related_ls]
        dic_bothive[key_dic]['related'] = {}
        for idx, v in enumerate(related):
            dic_bothive[key_dic]['related'][idx] = v

    if save:
        pickle_save('Bigwave-Robotics/Markets/Bothive/save/pickles/bothive_2depth.pkl', dic_bothive)
        json_save('Bigwave-Robotics/Markets/Bothive/save/json/bothive_2depth.json', dic_bothive)
    return dic_bothive

