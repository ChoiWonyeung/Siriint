import os
# url
url_page = "https://mall.daara.co.kr/product/list.html?cd=103100&rownum=100&page="

# 경로
# PATH = dotenv_values(".env")["PATH"]

path_pickles = os.path.abspath("Daara/pickles")
path_json = os.path.abspath("Daara/json")


ajax = 'http://mall.daara.co.kr/include/ajax_po_product.php?total_row=11&cd=103100&rownum=100&p_seq=101622&total_records=&page=1'