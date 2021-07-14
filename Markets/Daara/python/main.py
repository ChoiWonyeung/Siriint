import json
from common import *
from Markets.Daara.python.daara_1depth import crawl_key
from Markets.Daara.python.daara_2depth import crawl_detail
from Markets.Daara.python.daara_transform import trans

def __main__():
    depth1 = crawl_key(save=True, sample=True)
    dic_daara = crawl_detail(depth1, save=True)
    json_daara = trans(dic_daara)

    json_save('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Daara/json/result_daara.json', json_daara)

if __name__ == "__main__":
    # __main__()
    soup = req_bsEncoding('http://mall.daara.co.kr/product/view.html?cd=103100&rownum=100&page=1&p_seq=101621')
    a = soup.select('div.detailGoodsBox')
    div_table_page = a[0].select('div.pageNaviList')
    table_page_ls = div_table_page[0].select('ul.notranslate > li > a')
    table_page = [i['href'] for i in table_page_ls]
    soup_table = req_bsEncoding(table_page[0])
    div_table2 = soup_table.select('div.table')
    tbody = div_table2[0].select('tbody tr')
    td = tbody[0].select('td')
    a = [i.text.strip() for i in td]