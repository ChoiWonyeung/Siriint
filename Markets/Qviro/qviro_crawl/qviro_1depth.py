from common import *
import Markets.Qviro.qviro_configuration.qviro_config as config

'''
JSON 형태의 데이터로 수집 전체 프로세스는 같으나 방법이 조금 달라짐에 유의
'''

# 1차 크롤링 리스트
# product = []
# source = []
# company = []

# 2차 크롤링 딕셔너리
# dic_description = {}
# dic_spec = {}
# dic_image = {}

# 1차 크롤링 진행 (json 형태)


def crawl_json():
    source = []
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
    return dic_mainPage


for i in range(1, len(dic_pageMain) + 1):
    for j in range(len(dic_pageMain[i]['data'])):
        source.append(dic_pageMain[i]['data'][j]['url'])

if __name__ == '__main__':
    dic_mainPage = crawl_json()
    pickle_save(config.path_pickle + 'dic_mainPage.pkl', dic_mainPage)