import komachine_config as config
from Modules.common import *
import Modules.table_make
import re


def crawl_detail(result, sample=False, save=False):

    """
    komachine 수집 값의 dictionary(hash)를 만드는 함수.
    source(url, key)를 반복하여 접속하여 수집 항목에 따라 dictionary 구성
    정제 단계에서 모든 dictionary는 list 형태로 구성
    :param result:
    :param sample:
    :param save:
    :return:
    """

    cnt = 1
    for key, value in result.items():
        print(f"{cnt}번째 반복문 실행중...")

        soup = req_bsEncoding(key)
        sleep_random(print_time=True)

        result[key]['describe img'] = {}

        try:

            result[key]['catalog'] = {'{}'.format('pdf 파일'): '{}'.format(soup.select('div.product-doc a')[0]['href'])}
            result[key]['describe'] = {'{}'.format('제품 설명'): '{}'.format(soup.select('section.product-desc.fr-view p')[1].text.replace('\n', '').strip().replace(' ', ''))}

        except:

            result[key]['catalog'] = {}
            result[key]['describe'] = {'{}'.format('제품 설명'): '{}'.format(soup.select('section.product-desc.fr-view p')[1].text.replace('\n', '').strip().replace(' ', ''))}

        else:
            result[key]['catalog'] = {}
            result[key]['describe'] = {}


        img_list = []
        result[key]['img'] = {}

        try:

            result[key]['thumbnail'] = {'썸네일 이미지' : '{}'.format(soup.select('div.wrapper.img img')[0]['src'])}

        except:

            result[key]['thumbnail'] = {}

        img_list += [i['src'] for i in soup.select("div.product-detail-tab-contents img")]

        # 이미지 이름 넣는곳
        try:

            img_list_name = [i.text for i in soup.select('div.product-detail-tabs span')]
            result[key]['img'] = {'{}'.format(img_list_name[d]): '{}'.format(i) for d, i in enumerate(img_list)}

        except:

            result[key]['img'] = {'no_{}'.format(d): '{}'.format(i) for d, i in enumerate(img_list)}

        result[key]['brand'] = {'제조사': '{}'.format(i.replace('\n', '').strip()) for i in
                                (soup.select('div.title__short-desc div')[0])}

        result[key]['brand describe'] = {'제조사 설명': '{}'.format(i.replace('\n', '').strip()) for i in
                                         (soup.select('div.title__short-desc div')[1])}


        if cnt % 30 == 0 and save == True:
            print(f"{cnt} 번째에서 json 파일 생성중")
            json_save('./json/komachine_2depth.json', result)

        if sample == True and cnt != 30:
            cnt += 1
            continue

    return result


# import json
# with open('C:/Users/LG/Desktop/crolling/komachine/json/komachine_1depth.json', encoding='utf8') as json_file:
#     result = json.load(json_file)
#
# final_result_2 = crawl_detail(result, sample=True, save=True)