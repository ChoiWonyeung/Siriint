import thinksolutions_config as config
from common import *
from table_make import table_make
import re


# with open(config.path_json + '/1depth.json') as json_file:
#     result = json.load(json_file)
'''
len(result)




cnt = 1

"https://thinkbotsolutions.com//collections/all/products/onrobot-rg2-fingertips"

div_list = soup.select('.product-gallery__carousel-item div')

result["https://thinkbotsolutions.com//collections/all/products/onrobot-rg2-fingertips"].select('img')[i]['src'].split('/products/')[0]

if remind == div_list[i].select('img')[0]['src'].split('/products/')[1]:
    pass
else:
    print(div_list[i].select('img')[0]['src'])
    description_list.append(div_list[i].select('img')[0]['src'])

remind = div_list[i].select('img')[0]['src'].split('/products/')[1]
'''




def crawl_detail(result, sample=False, save=False):
    cnt = 1

    for key, value in result.items():
        print(f"{cnt}번째 반복문 실행중...")

        soup = req_bsEncoding(key)
        sleep_random(2, 4, print_time=True)

        remind = ''
        description_list = []
        result[key]['image'] = {}
        div_list = soup.select('.product-gallery__carousel-item div')

        for i in range(int(len(div_list))):
            if remind == div_list[i].select('img')[0]['src'].split('/products/')[1]:
                continue
            else:
                description_list.append(div_list[i].select('img')[0]['src'])

            remind = div_list[i].select('img')[0]['src'].split('/products/')[1]

        result[key]['image'] = {'{}'.format(d): 'http:{}'.format(i) for d, i in enumerate(description_list)}

        product_number = soup.select('section.section')[0]['data-section-settings'].replace('\n', '').replace(' ', '').split(',')[2].split(':')[1]

        try:
            result[key]["option"] = {
                'option {}'.format(d): i['value'] for d, i in
                enumerate(soup.select('select.product-form__single-selector')[0])}

            result[key]["price"] = {
                'option {}'.format(d): '${}'.format(i.text.split('$')[1]) for d, i in
                enumerate(soup.select('select#product-select-' + product_number)[0])}

            result[key]["type"] = \
            ['>'.join([j for j in i.text.split('\n') if j]) for i in soup.select('ol.breadcrumb__list')][0]

            result[key]['Description'] = ' '.join(
                [soup.select('div.rte.text--pull p')[i].text for i in range(len(soup.select('div.rte.text--pull p')))])
        except:

            try:
                result[key]["option"] = {}

                result[key]["price"] = {'NO Option' : '{}'.format(soup.select('span.price')[0].text)}

                if type(result[key]["price"]) == set:
                    result[key]["price"] = {'NO Option': '{}'.format(soup.select('span.price')[0].text)}

                result[key]["type"] = \
                    ['>'.join([j for j in i.text.split('\n') if j]) for i in soup.select('ol.breadcrumb__list')][0]

                result[key]['Description'] = ' '.join(
                    [soup.select('div.rte.text--pull p')[i].text for i in range(len(soup.select('div.rte.text--pull p')))])

            except:
                result[key]["option"] = {}

                result[key]["price"] = {}

                result[key]["type"] = \
                    ['>'.join([j for j in i.text.split('\n') if j]) for i in soup.select('ol.breadcrumb__list')][0]

                result[key]['Description'] = ' '.join(
                    [soup.select('div.rte.text--pull p')[i].text for i in
                     range(len(soup.select('div.rte.text--pull p')))])

        cnt += 1

    if save == True:
        json_save('./json/thinkbotsolutions_2depth.json', result)

    return result

#
# dic_daara = crawl_detail(result,sample=True, save=True)
#
#
#
# json_save(config.path_json + '/2depth.json', dic_daara)
#
# dic_daara['https://thinkbotsolutions.com//collections/all/products/weiss-robotics-gripkit-pz1']
#
# type(dic_daara['https://thinkbotsolutions.com//collections/all/products/weiss-robotics-gripkit-pz1']['price']) == set
#
#
# key = 'https://thinkbotsolutions.com//collections/all/products/onrobot-flange-adapter-kit'
#
# soup = req_bsEncoding(key)
#         sleep_random(print_time=True)
#
#         remind = ''
#         description_list = []
#         result[key]['image'] = {}
#         div_list = soup.select('.product-gallery__carousel-item div')
#
#         for i in range(int(len(div_list))):
#             if remind == div_list[i].select('img')[0]['src'].split('/products/')[1]:
#                 continue
#             else:
#                 description_list.append(div_list[i].select('img')[0]['src'])
#
#             remind = div_list[i].select('img')[0]['src'].split('/products/')[1]
#
#         result[key]['image'] = {'{}'.format(d) : 'http:{}'.format(i) for d,i in  enumerate(description_list)}
#
#         product_number = soup.select('section.section')[0]['data-section-settings'].replace('\n', '').replace(' ', '').split(',')[2].split(':')[1]
#
#         result[key]["option"] = {
#                 'option {}'.format(d): i['value'] for d, i in
#                 enumerate(soup.select('select.product-form__single-selector')[0])}
#
#             result[key]["price"] = {
#                 'option {}'.format(d): '${}'.format(i.text.split('$')[1]) for d, i in
#                 enumerate(soup.select('select#product-select-' + product_number)[0])}
#
#             result[key]["type"] = \
#             ['>'.join([j for j in i.text.split('\n') if j]) for i in soup.select('ol.breadcrumb__list')][0]
#
#             result[key]['Description'] = ' '.join(
#                 [soup.select('div.rte.text--pull p')[i].text for i in range(len(soup.select('div.rte.text--pull p')))])
