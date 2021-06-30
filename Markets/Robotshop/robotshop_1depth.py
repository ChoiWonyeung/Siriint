from common import *
import robotshop_config

# webdriver 불러오기
driver = get_webdriver(path_webdriver)

# 1차 크롤링 항목 (Key 항목 + @)
source = []

# source 수집 (key)
cnt = 0
page = 1
except_num = 1

while cnt <= 5:
    print(f'{page}페이지 수집중...')
    soup = sel_bsEncoding((robotshop_config.dic_url[cnt] + str(page)))
    sleep_random(2, 10, print_time=True)
    source += ls_driverHref(robotshop_config.selector_source)
    print('--------------------------------------------------------')

    if ls_driverHref(robotshop_config.selector_source) != []:  # 페이지에서 수집 요소가 없을경우
        page += 1
    else:
        print(f'Except occurred : {except_num}')
        except_num += 1
        cnt += 1
        page = 1

# 2차 크롤링

dic_robotshop = {}
for url2 in source:
    dic_robotshop[url2] = dic_bigWaveRobotics()
    sel_bsEncoding(url2)
    sleep_random(print_time=True)

    for key in robotshop_config.dic_selector.keys():
        if key == 'image':
            try:
                dic_robotshop[url2][key] = ls_driverFinder(robotshop_config.dic_selector[key], 'data-src')
            except Exception as e0:
                print('Error occurred', key, e0)
                pass

        elif key == 'catalog':
            try:
                dic_robotshop[url2][key] = ls_driverHref(robotshop_config.dic_selector[key])
            except Exception as e1:
                print('Error occurred', key, e1)
                pass

        else:
            try:
                dic_robotshop[url2][key] = driverText(robotshop_config.dic_selector[key])
            except Exception as e2:
                print('Error occurred', key, e2)
                pass

pickle_save('dic_robotshop.pkl', dic_robotshop)