from common import *
import Markets.Bothive.bothive_configuration.bothive_config as config

dic_bothive = pickle_load(config.path_pickle + 'dic_bothive.pkl')


def postProcess(dic_bothive):
    str_match = {}
    for dic_key, value in dic_bothive.items():

        for Str in value['delivery']:
            if 'Price' in Str:
                try:
                    str_match[dic_key] = [Str]
                except Exception as e:
                    print(e)

        for i in str_match.keys():
            dic_bothive[i]['price'] = str_match[i]
    return dic_bothive
