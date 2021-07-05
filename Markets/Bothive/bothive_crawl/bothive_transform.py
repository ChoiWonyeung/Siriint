from common import *
import Markets.Bothive.bothive_configuration.bothive_config as config
from ETC import format_json
from Markets.Bothive.bothive_crawl.bothive_postprocess import postProcess, dic_bothive

def trans(dic_bothive):
    json_bothive = {}
    for K, V in dic_bothive.items():
        json_bothive[K] = format_json.format_json(K)
        json_bothive[K]['brand'] = dic_bothive[K]['brand'][0]

        try:
            json_bothive[K]['description'] = V['description1']
        except Exception as e:
            print(e)

        try:
            json_bothive[K]['shipping'] = V['delivery']
        except Exception as e:
            print(e)

        try:
            json_bothive[K]['model_name'] = {'': V['product']}
        except Exception as e:
            print(e)

        try:
            json_bothive[K]['summary'] = {'{lang}' + str(j): dic_bothive[K]['highlight'][j] for j in range(len(dic_bothive[K]['highlight']))}
        except Exception as e:
            print(e)

        if len(dic_bothive[K]['price']) >= 1:
            try:
                json_bothive[K]['price']['original'] = dic_bothive[K]['price'][0]
            except Exception as e:
                print(e)

        for i in dic_bothive[K]['spec']:
            if 'Payload' in i:
                try:
                    json_bothive[K]['payload'] = {'': i}
                except Exception as e:
                    print(e)

            if 'Reach' in i:
                try:
                    json_bothive[K]['reach'] = {'': i}
                except Exception as e:
                    print(e)

            if 'Weight' in i:
                try:
                    json_bothive[K]['weight'] = {'': i}
                except Exception as e:
                    print(e)
    return json_bothive
