from common import *
import Markets.Qviro.qviro_configuration.qviro_config as config


def crawl_json(sample=False, save=False):
    """

    :param sample:
    :param save:
    :return:
    """
    dic_mainPage = {}
    num_page = 1
    while True:
        req = requests.get(config.url + str(num_page))
        dic_mainPage[num_page] = req.json()
        sleep_random(print_time=True)
        if num_page >= 2 and dic_mainPage[num_page]['data'] == dic_mainPage[num_page - 1]['data']:
            del dic_mainPage[num_page]
            break
        else:
            num_page += 1
        # return dic_mainPage

    dic_qviro = {}
    if sample:
        for i in range(1, 3):
            for j in range(10):
                dic_qviro[dic_mainPage[i]['data'][j]['url']] = {}

    else:
        for i in range(1, len(dic_mainPage) + 1):
            for j in range(len(dic_mainPage[i]['data'])):
                dic_qviro[dic_mainPage[i]['data'][j]['url']] = {}

    if save:
        pickle_save('../pickles/qviro_1depth.pkl', dic_qviro)
        json_save('../json/qviro_1depth.json', dic_qviro)

    return dic_qviro


if __name__ == '__main__':
    dic_qviro = crawl_json(save=True, sample=True)