from common import *
import Markets.Qviro.qviro_configuration.qviro_config as config

def crawl_detail(dic_qviro, save=False):

    for dic_key in dic_qviro.keys():
        soup = req_bsEncoding(dic_key)
        sleep_random(2, 4, print_time=True)

        # 타입 긁기
        ul_ls = soup.select('ul.breadcrumbs')
        li_ls = ul_ls[0].select('li')
        type = li_ls[0].text.strip()
        brand = li_ls[1].text.strip()

        dic_qviro[dic_key]['type'] = type
        dic_qviro[dic_key]['brand'] = brand

        product = [li_ls[2].text.strip()]
        dic_qviro[dic_key]['product'] = {}
        for idx, v in enumerate(product):
            dic_qviro[dic_key]['product'][idx] = v

        # 이미지, 비디오 긁기
        div_image = soup.select('div.product-slider.product-slider-for')

        # 비디오 수집
        video_ls = div_image[0].select('div > iframe')
        video = [i['src'] for i in video_ls]
        dic_qviro[dic_key]['video'] = {}
        # for idx, v in enumerate(video):
        #     dic_qviro[dic_key]['video'][idx] = v

        # 이미지 수집
        image_ls = div_image[0].select('div > img')
        image = [i['src'] for i in image_ls]
        dic_qviro[dic_key]['image'] = {}

        thumbnail1 = image + video
        thumbnail = ', '.join(thumbnail1)
        dic_qviro[dic_key]['thumbnail'] = thumbnail

        # for idx, v in enumerate(image):
        #     dic_qviro[dic_key]['image'][idx] = v

        # 제품 정보 긁기
        div_description = soup.select('div.product-tab-contents')

        description_img1 = div_description[0].select('img')
        description_img = [i['src'] for i in description_img1]

        description_ls = div_description[0].select('div.product-description > p')
        description = [i.text.strip() for i in description_ls]

        dic_qviro[dic_key]['description_img'] = description_img
        dic_qviro[dic_key]['description'] = description


        # 스펙(테이블)
        table_ls = soup.select('table')
        tr_ls = table_ls[0].select('td')
        tr = [i.text.strip() for i in tr_ls]
        th = []
        td1 = []
        td = []
        for idx, value in enumerate(tr):
            if idx % 2 == 0:
                th.append(value)
            elif idx % 2 == 1:
                td1.append(value)
        for i in td1:
            td.append(i.replace('\n', ' '))
        spec = dict(zip(th, td))

        dic_qviro[dic_key]['spec'] = spec

        # Usecases
        try:
            usecase_ls = soup.select('#useCases')

            # usecase 비디오
            usecase_video1 = usecase_ls[0].select('iframe')
            usecase_video = [i['src'] for i in usecase_video1]
            dic_qviro[dic_key]['usecase_video'] = {}
            for idx, v in enumerate(usecase_video):
                dic_qviro[dic_key]['usecase_video'][idx] = v


            usecase_text_ls = usecase_ls[0].select('div.carousel-item')
            usecase_text1 = [i.text.strip() for i in usecase_text_ls]
            usecase_text2 = [i.replace('\n', ' ').replace('\t', '') for i in usecase_text1]
            usecase_text = {}
            for idx, v in enumerate(usecase_text2):
                usecase_text[idx] = v
            dic_qviro[dic_key]['usecase_text'] = usecase_text

        except:
            pass

    if save:
        pickle_save('./pickles/qviro_2depth.pkl', dic_qviro)
        json_save('./json/qviro_2depth.json', dic_qviro)
    return dic_qviro


# if __name__ == '__main__':
