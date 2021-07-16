from common import *
import Markets.Bothive.configuration.bothive_config as config

# dic_bothive = pickle_load(config.path_pickles + '/dic_bothive_2depth.pkl')

def postProcess(dic_bothive, save=False):
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

    if save == True:
        json_save(config.path_json + '/dic_bothive_postProcess.json', dic_bothive)
    return dic_bothive


dic_bothive3 = postProcess(dic_bothive)
pickle_save(config.path_pickles + '/dic_bothive_postProcess.pkl', dic_bothive3)