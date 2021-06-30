import daara_config
from common import *
from copy import deepcopy
import json
import BWR_json
from daara_2depth import key_crawling, detail_crawling

def abc():
    # dictionary 불러오기
    dic_daara = pickle_load('/Users/kimkangnam/Desktop/dic_daara2.pkl')
    source = pickle_load('/Users/kimkangnam/Desktop/source.pkl')

    print(dic_daara['http://mall.daara.co.kr/product/view.html?cd=103100&page=40&p_seq=48701'])

    # #백업 만들기
    # dic_daara_backup = deepcopy(dic_daara)
    #
    # # 데이터 정보 파싱
    # for i in source:
    #     #     try:
    #     #         dic_daara[i]['delivery'] = dic_daara[i]['seller'][3]
    #     #         dic_daara[i]['seller'] = dic_daara[i]['seller'][:3]
    #     #     except Exception as e0:
    #     #         print('Error occurred, i, e0)
    #     #         pass
    #
    #     # try:
    #     #     dic_daara[i]['seller'][0] = dic_daara[i]['seller'][0].split('\n')
    #     # except Exception as e1:
    #     #     print('Error occurred', i, e1)
    #     #     pass
    #
    #     try:
    #         dic_daara[i]['seller'][0] = list(filter(None, dic_daara[i]['seller'][0]))
    #     except Exception as e2:
    #         print('Error occurred', i, e2)
    #         pass
    #
    #     try:
    #         dic_daara[i]['seller'] = dic_daara[i]['seller'][0]
    #     except Exception as e3:
    #         print('Error occurred', i, e3)
    #         pass
    #
    #     dic_daara[i]['order'][0] = dic_daara[i]['order'][0].replace(u'\xa0', u'')
    #     dic_daara[i]['order'][1] = dic_daara[i]['order'][1].replace(u'\xa0', u'')
    #     # dic_daara[i]['type1'] = dic_daara[i]['type1'][0]
    #     # dic_daara[i]['type2'] = dic_daara[i]['type2'][0]
    #     dic_daara[i]['description1'] = list(filter(None, dic_daara[i]['description1'][0].split('\n')))[1:]
    #     dic_daara[i]['description2'] = list(filter(None, dic_daara[i]['description2'][0].split('\n')))[1:]
    #
    #     for j in range(len(dic_daara[i]['description2'])):
    #         dic_daara[i]['description2'][j] = dic_daara[i]['description2'][j].strip()
    #
    #     del dic_daara[i]['description2'][1]
    #
    # # csv화
    # df_daara = pd.DataFrame(dic_daara)
    # df_daara = df_daara.transpose()
    # df_daara.reset_index(inplace=True)
    # df_daara.rename(columns={'index': 'source'}, inplace=True)
    #
    # json_daara = {}
    # for i in source:
    #     json_daara[i] = BWR_json.BWR_json(i)
    #     json_daara[i]['brand'] = dic_daara[i]['brand']
    #
    # # pickle_save('df_daara.pkl', df_daara)
    # # df_daara.to_csv('/Users/kimkangnam/Desktop/daara_data.csv')
    #
    # # with open('/Users/kimkangnam/Desktop/BRW_daara_sample_json', 'w', encoding='utf-8') as file_json:
    # #     json.dump(dic_daara, file_json, indent='\t', ensure_ascii=False)

if __name__ == "__main__":
    # source, product, brand, price = key_crawling()
    # dic_daara = detail_crawling(source, product, brand, price)
    abc()
    # pickle_save('dic_daara.plk', dic_daara)