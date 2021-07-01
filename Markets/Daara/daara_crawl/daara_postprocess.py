import daara_configuration.daara_config as config
from common import *


# description1 정제
def pp_description1(source, dic_daara):
    """
    description1 항목에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    for i in source:
        try:
            dic_daara[i]['description1'][0] = dic_daara[i]['description1'][0].split('\n')
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['description1'][0] = list(filter(None, dic_daara[i]['description1'][0]))
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['description1'] = dic_daara[i]['description1'][0][1:]
        except Exception as e:
            print(e)
    return dic_daara


# description2 정제
def pp_description2(source, dic_daara):
    """
    description2에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    for i in source:
        try:
            dic_daara[i]['description2'] = dic_daara[i]['description2'][0].split('\n')
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['description2'] = list(filter(None, dic_daara[i]['description2']))
        except Exception as e:
            print(e)

        try:
            del dic_daara[i]['description2'][0], dic_daara[i]['description2'][1]
        except Exception as e:
            print(e)

        for j in range(len(dic_daara[i]['description2'])):
            try:
                dic_daara[i]['description2'][j] = dic_daara[i]['description2'][j].strip()
            except Exception as e:
                print(e)
    return dic_daara


# order 정제
def pp_order(source, dic_daara):
    """
    order 항목에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    for i in source:
        try:
            dic_daara[i]['order'][0] = dic_daara[i]['order'][0].replace(u'\xa0', u'')
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['order'][1] = dic_daara[i]['order'][1].replace(u'\xa0', u'')
        except Exception as e:
            print(e)
    return dic_daara


# delivery 정제
def pp_delivery(source, dic_daara):
    """
    delivery 항목에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    for i in source:
        if dic_daara[i]['delivery'] == []:
            try:
                dic_daara[i]['delivery'] = [dic_daara[i]['seller'][3]]
            except Exception as e:
                print(e)

        try:
            dic_daara[i]['delivery'] = dic_daara[i]['delivery'][0].split('\n')
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['delivery'] = list(filter(None, dic_daara[i]['delivery']))
        except Exception as e:
            print(e)

        for j in range(len(dic_daara[i]['delivery'])):
            try:
                dic_daara[i]['delivery'][j] = dic_daara[i]['delivery'][j].strip()
            except Exception as e:
                print(e)
    return dic_daara


# seller 정제
def pp_seller(source, dic_daara):
    """
    seller 항목에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    for i in source:
        if dic_daara[i]['deilvery'] == []:
            try:
                dic_daara[i]['delivery'] = [dic_daara[i]['seller'][3]]
            except Exception as e:
                print(e)

        try:
            dic_daara[i]['seller'] = dic_daara[i]['seller'][:3]
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['seller'] = dic_daara[i]['seller'][0].split('\n')
        except Exception as e:
            print(e)

        try:
            dic_daara[i]['seller'] = list(filter(None, dic_daara[i]['seller']))
        except Exception as e:
            print(e)
    return dic_daara
