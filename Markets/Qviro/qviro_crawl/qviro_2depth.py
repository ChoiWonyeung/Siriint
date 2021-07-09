from common import *
import Markets.Qviro.qviro_configuration.qviro_config as config

dic_pageMain = pickle_load('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Qviro/qviro_pickle/dic_mainPage.pkl')





dic_qviro = {}
for url2 in source[:3]:
    dic_qviro[url2] = dic_bigWaveRobotics()
    soup = req_bsEncoding(url2)
    sleep_random(print_time=True)

    # try:
    #     dic_qviro[url2]['image'] = ls_srcmake(soup, config.selector_image)
    # except Exception as e:
    #     print(e)

    try:
        dic_qviro[url2]['spec'] = textmake(soup, config.selector_spec)
    except Exception as e:
        print(e)

    try:
        dic_qviro[url2]['description1'] = textmake(soup, config.selector_description)
    except Exception as e:
        print(e)


for i in range(1, len(dic_pageMain) + 1):
    for j in range(len(dic_pageMain[i]['data'])):
        if dic_qviro[]
        dic_qviro[]dic_pageMain[i]['data'][j]['image']

# # 2차 크롤링 진행
# for url2 in df_qviro['source']:
#     soup = sel_bsEncoding(url2)
#     sleep_random()
#
#     try:
#         # 수집
#         dic_description[url2] = textmake(qviro_config.selector_description, normalize_unicode=True, makeList=False)
#         dic_spec[url2] = textmake(qviro_config.selector_spec, makeList=False)
#         dic_image[url2] = ls_driverSrc(qviro_config.selector_image)
#         # 구성
#         df_qviro['description1'] = df_qviro['source'].map(dic_description)
#         df_qviro['spec'] = df_qviro['source'].map(dic_spec)
#         df_qviro['image'] = df_qviro['source'].map(dic_image)
#
#         # 데이터 저장
#         df_qviro.to_csv('/Users/kimkangnam/Desktop/quivro_v0.0.2.csv', encoding='utf-8')
#
#     except Exception:
#         print('Exception occurred')
#         pass
