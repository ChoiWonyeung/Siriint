from ETC import format_json

# dic_bothive = pickle_load(config.path_pickles + '/dic_bothive_postProcess.pkl')

def trans(dic_bothive):
    """
    dic_bothive를 수요업체측의 양식인 json_bothive로 맞추는 함수
    :param dic_bothive:
    :return:
    """
    json_bothive = {}
    for dic_key, dic_value in dic_bothive.items():
        json_bothive[dic_key] = format_json.format_json(dic_key)
        json_bothive[dic_key]['name'] = dic_bothive[dic_key]['product'][0]
        json_bothive[dic_key]['brand'] = dic_bothive[dic_key]['brand'][0]
        json_bothive[dic_key]['type'] = dic_bothive[dic_key]['type'][0]
        json_bothive[dic_key]['thumbnail'] = dic_bothive[dic_key]['image'][0]
        json_bothive[dic_key]['summary'][0] = dic_bothive[dic_key]['highlight']
        json_bothive[dic_key]['warranty']['Servicing (Months)'] = dic_bothive[dic_key]['highlight']['Servicing (Months)']
        json_bothive[dic_key]['description'][0] = dic_value['description'][0]

        str_match = {}
        for Str in dic_value['delivery']:
            if 'Price' in Str:
                try:
                    str_match[dic_key] = [Str]
                except Exception as e:
                    print(e)

        for i in str_match.keys():
            json_bothive[dic_key]['price']['original'] = str_match[i][0]
    return json_bothive
