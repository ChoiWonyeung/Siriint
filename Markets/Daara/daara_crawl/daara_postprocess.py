import daara_configuration.daara_config as config
from common import *


# description1 정제
def pp_description1(dic_daara):
    """
    description1 항목에 대한 정제
    :param dic_daara:
    :return:
    """
    dsc1 = 'description1'
    for key, value in dic_daara.items():
        try:
            value[dsc1][0] = value[dsc1][0].split('\n')
        except Exception as e:
            print(e)

        try:
            value[dsc1][0] = list(filter(None, value[dsc1][0]))
        except Exception as e:
            print(e)

        try:
            value[dsc1] = value[dsc1][0][1:]
        except Exception as e:
            print(e)

        try:
            value[dsc1][0] = value[dsc1][0].split()
        except Exception as e:
            print(e)

        for j in range(len(value[dsc1][0])):
            try:
                value[dsc1].insert(j, value[dsc1][j][j])
            except Exception as e:
                print(e)

        try:
            for idx, desc in enumerate(value[dsc1]):
                if type(desc) == type(list()):
                    value[dsc1].pop(idx)
        except Exception as e:
            print(e)
    return dic_daara


# description2 정제
def pp_description2(dic_daara):
    """
    description2에 대한 정제
    :param dic_daara:
    :return:
    """
    dsc2 = 'description2'
    for key, value in dic_daara.items():
        try:
            value[dsc2] = value[dsc2][0].split('\n')
        except Exception as e:
            print(e)

        try:
            value[dsc2] = list(filter(None, value[dsc2]))
        except Exception as e:
            print(e)

        try:
            del value[dsc2][0], value[dsc2][1]
        except Exception as e:
            print(e)

        for j in range(len(value[dsc2])):
            try:
                value[dsc2][j] = value[dsc2][j].strip()
            except Exception as e:
                print(e)

        try:
            value[dsc2][0] = value[dsc2][0].split(' ', 1)
        except Exception as e:
            print(e)

        for j in range(len(value[dsc2][0])):
            try:
                value[dsc2].insert(j, value[dsc2][j][j])
            except Exception as e:
                print(e)

        for idx, desc in enumerate(value[dsc2]):
            try:
                if type(desc) == type(list()):
                    value[dsc2].pop(idx)
            except Exception as e:
                print(e)

    return dic_daara


# order 정제
def pp_order(dic_daara):
    """
    order 항목에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    ord = 'order'
    for key, value in dic_daara.items():
        try:
            value[ord][0] = value[ord][0].replace(u'\xa0', u'')
        except Exception as e:
            print(e)

        try:
            value[ord][1] = value[ord][1].replace(u'\xa0', u'')
        except Exception as e:
            print(e)
    return dic_daara


# delivery 정제
def pp_delivery(dic_daara):
    """
    delivery 항목에 대한 정제
    :param source:
    :param dic_daara:
    :return:
    """
    deliv = 'delivery'
    for key, value in dic_daara.items():
        if value[deliv] == []:
            try:
                value[deliv] = [value['seller'][3]]
            except Exception as e:
                print(e)

        try:
            value[deliv] = value[deliv][0].split('\n')
        except Exception as e:
            print(e)

        try:
            value[deliv] = list(filter(None, value[deliv]))
        except Exception as e:
            print(e)

        for j in range(len(value[deliv])):
            try:
                value[deliv][j] = value[deliv][j].strip()
            except Exception as e:
                print(e)
    return dic_daara


# seller 정제
def pp_seller(dic_daara):
    """
    seller 항목에 대한 정제
    :param dic_daara:
    :return:
    """
    sell = 'seller'
    for key, value in dic_daara.items():
        if value['delivery'] == []:
            try:
                value['delivery'] = [value[sell][3]]
            except Exception as e:
                print(e)

        try:
            value[sell] = value[sell][:3]
        except Exception as e:
            print(e)

        try:
            value[sell] = value[sell][0].split('\n')
        except Exception as e:
            print(e)

        try:
            value[sell] = list(filter(None, value[sell]))
        except Exception as e:
            print(e)
    return dic_daara


if __name__ == '__main__':
    dic_daara = pickle_load(config.path_pickle + 'dic_daara.pkl')
    source = pickle_load(config.path_pickle + 'source.pkl')

    dic_daara = pp_description1(dic_daara)
    dic_daara = pp_description2(dic_daara)
    dic_daara = pp_order(dic_daara)
    dic_daara = pp_delivery(dic_daara)
    dic_daara = pp_seller(dic_daara)