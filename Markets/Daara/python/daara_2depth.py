import config as config
from Modules.common import *
from Modules.table_make import table_make
import re


def crawl_detail(result, sample=False, save=False):
    """
    다아라 수집 값의 dictionary(hash)를 만드는 함수.
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

        # description crawling
        div_list = soup.select('div.detailInfoBox')[0]
        description1 = div_list.select('#detailInfoTab0 img')
        description2 = div_list.select('#detailInfoTab1 img')
        description_list = description1 + description2
        result[key]['description'] = {}
        for idx, description in enumerate(description_list):
            result[key]['description'][idx] = f'http:{description["src"]}'

        # option crawling
        result[key]["option"] = table_make(soup)

        # catalog crawling
        catalog_list = soup.select("a.btn-down")
        result[key]["catalog"] = []
        for catalog in catalog_list:
            result[key]["catalog"].append(catalog["href"])

        # image crawling
        image_list = soup.select("div.detailTopImg > img")
        images = []
        for image in image_list:
            images.append(image["src"])
        for image_src in images:
            result[key]["image"] = f"http:{image_src}"

        # category crawling
        li_list = soup.select("div.pageInfoNav > div.fixlayout > ul > li")
        category = ""
        for i, li in enumerate(li_list):
            if i > 0:
                text = li.text.strip()
                text = re.sub('>', " > ", text)
                category += f"{text}"
        result[key]["category"] = category

        # highlight crawling
        li_list = soup.select(".goodsDetail > li")
        highlight_dict = {}
        for idx, li in enumerate(li_list):
            text = li.text.strip()
            highlight_dict[str(idx)] = text
        result[key]["highlight"] = highlight_dict

        # order carwling
        li_list = soup.select(".num_dc > li")
        order_dict = {}
        for li in li_list:
            text_list = re.split(":", li.text)
            if len(text_list) > 1:
                li_key = text_list[0].strip()
                li_value = text_list[1].strip()
                order_dict[li_key] = li_value
            else:
                order_dict[text_list[0]] = ""
        result[key]["order"] = order_dict

        # 반품 / 교환 crawling
        table_list = soup.select("#detailInfoTab5 table")
        h4_list = soup.select("#detailInfoTab5 h4")

        for idx, table in enumerate(table_list):
            h4 = h4_list[idx].text.strip()
            th_list = table.select("th")
            td_list = table.select("td")
            table_dict = {}

            for j in range(len(th_list)):
                th = th_list[j].text.strip()
                td = td_list[j].text.strip()
                td = re.sub("\r|\n", "", td)
                td = " ".join(td.split())
                table_dict[th] = td
            result[key][h4] = table_dict

        if cnt % 10 == 0 and save == True:
            print(f"{cnt} 번째에서 json 파일 생성중")
            json_save(config.path_json + '/2depth.json', result)

        if sample == True and cnt == 20:
            cnt += 1
            continue

        break
    return result

if __name__ == '__main__':
    pass