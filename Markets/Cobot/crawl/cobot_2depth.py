from common import *


def crawl_detail(dic_cobot, save=False, sample=False):
    cnt = 1
    for dic_key, dic_value in dic_cobot.items():
        print(f'{cnt}번째 크롤링')
        soup = req_bsEncoding(dic_key)
        sleep_random(print_time=True)

        # 콘텐츠 집합
        content = soup.select('.content-area')

        # 이미지 크롤링
        div_image = content[0].select('div.img-thumbnail >div.inner > img')
        image1 = [i['href'] for i in div_image]
        image = ','.join(image1)
        dic_cobot[dic_key]['thumbnail'] = image

        # 개략 정보
        div_summary = content[0].select('div.summary')

        # 제품명
        product_name_ls = div_summary[0].select('h2')
        product_name1 = [product_name_ls[0].text.strip()]
        product_name = {}
        for idx, v in enumerate(product_name1):
            product_name[idx] = v
        dic_cobot[dic_key]['name'] = product_name

        # 카테고리
        category_ls = div_summary[0].select('span.tagged_as > a')
        category1 = [i.text.strip() for i in category_ls]
        category = {}
        dic_cobot[dic_key]['summary'] = {}
        for idx, v in enumerate(category1):
            category[idx] = v
        dic_cobot[dic_key]['summary'] = category

        # 모델명
        sku_ls = div_summary[0].select('span.sku')
        sku1 = [i.text.strip() for i in sku_ls]
        sku = {}
        for idx, v in enumerate(sku1):
            sku[idx] = v
        dic_cobot[dic_key]['model_name'] = sku

        # 옵션
        option_ls = div_summary[0].select('td.value > select > option')
        option1 = [i.text.strip() for i in option_ls]
        option = {}
        for idx, v in enumerate(option1):
            option[idx] = v
        dic_cobot[dic_key]['options'] = option

        # 상세 정보
        div_body = content[0].select('div.resp-tabs-container')

        # description
        description_ls = content[0].select('div.resp-tabs-container p')
        description1 = [i.text.strip() for i in description_ls]
        description2 = list(filter(None, description1))
        description = {}
        for idx, v in enumerate(description2):
            description[idx] = v
        dic_cobot[dic_key]['description'] = description

        # related
        # div_related = soup.select('div.related')
        # related_ls = div_related[0]('div.owl-stage-outer div a')
        # related = [i['href'] for i in related_ls]
        # dic_cobot[dic_key]['related'] = {}
        # for idx, v in enumerate(related):
        #     dic_cobot[dic_key]['relataed'][idx] = v

        # spec
        try:
            table_ls = div_body[0].select('table')
            th_ls = table_ls[0].select('th')
            th = [i.text.strip() for i in th_ls]
            td_ls = table_ls[0].select('td')
            td = [i.text.strip() for i in td_ls]
            table = dict(zip(th, td))

            dic_cobot[dic_key]['dimension'] = table
        except Exception:
            pass
        if sample == True | cnt == 30:
            break
        cnt += 1
    if save== True:
        json_save('./json/cobot_2depth.json', dic_cobot)
        pickle_save('./pickles/dic_cobot_2depth.pkl', dic_cobot)
    return dic_cobot