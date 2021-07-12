from common import *
import Markets.Qviro.qviro_configuration.qviro_config as config

dic_qviro = pickle_load('../pickles/qviro_1depth.pkl')

# for dic_key in dic_qviro.keys():
#     soup = req_bsEncoding(dic_key)
#     sleep_random(2, 4, print_time=True)

soup = req_bsEncoding('https://qviro.com/product/ur5e')

# 타입 긁기
ul_ls = soup.select('ul.breadcrumbs')
li_ls = ul_ls[0].select('li')
type = li_ls[0].text.strip()
brand = li_ls[1].text.strip()
product = li_ls[2].text.strip()

# 이미지, 비디오 긁기
div_image = soup.select('div.product-slider.product-slider-for')

image_ls = div_image[0].select('div > img')
video_ls = div_image[0].select('div > iframe')

image = [i['src'] for i in image_ls]
video = [i['src'] for i in video_ls]

# 제품 정보 긁기
div_description = soup.select('div.product-tab-contents')

description_img1 = div_description[0].select('img')
description_img = [i['src'] for i in description_img1]

description_ls = div_description[0].select('div.product-description > p')
description = [i.text.strip() for i in description_ls]

# 스펙(테이블)
table_ls = soup.select('table')
tr_ls = table_ls[0].select('td')
tr = [i.text.strip() for i in tr_ls]
th = []
td = []
for idx, value in enumerate(tr):
    if idx % 2 == 0:
        th.append(value)
    elif idx % 2 == 1:
        td.append(value)
spec = dict(zip(th, td))

# Usecases
usecase_ls = soup.select('#useCases')
usecase_video1 = usecase_ls[0].select('iframe')
usecase_text1 = usecase_ls[0].select('p')

usecase_video = [i['src'] for i in usecase_video1]
usecase_text = [i.text.strip() for i in usecase_text1]




# for idx, v in enumerate(image_ls):
#     dic_qviro[dic_key]['image'] = {}
#     dic_qviro[dic_key]['image'][idx] = v['src']


#     # try:
#     #     dic_qviro[url2]['image'] = ls_srcmake(soup, config.selector_image)
#     # except Exception as e:
#     #     print(e)
#
#     try:
#         dic_qviro[url2]['spec'] = textmake(soup, config.selector_spec)
#     except Exception as e:
#         print(e)
#
#     try:
#         dic_qviro[url2]['description1'] = textmake(soup, config.selector_description)
#     except Exception as e:
#         print(e)
#
#
# for i in range(1, len(dic_pageMain) + 1):
#     for j in range(len(dic_pageMain[i]['data'])):
#         if dic_qviro[]
#         dic_qviro[]dic_pageMain[i]['data'][j]['image']
#
# # # 2차 크롤링 진행
# # for url2 in df_qviro['source']:
# #     soup = sel_bsEncoding(url2)
# #     sleep_random()
# #
# #     try:
# #         # 수집
# #         dic_description[url2] = textmake(qviro_config.selector_description, normalize_unicode=True, makeList=False)
# #         dic_spec[url2] = textmake(qviro_config.selector_spec, makeList=False)
# #         dic_image[url2] = ls_driverSrc(qviro_config.selector_image)
# #         # 구성
# #         df_qviro['description1'] = df_qviro['source'].map(dic_description)
# #         df_qviro['spec'] = df_qviro['source'].map(dic_spec)
# #         df_qviro['image'] = df_qviro['source'].map(dic_image)
# #
# #         # 데이터 저장
# #         df_qviro.to_csv('/Users/kimkangnam/Desktop/quivro_v0.0.2.csv', encoding='utf-8')
# #
# #     except Exception:
# #         print('Exception occurred')
# #         pass
