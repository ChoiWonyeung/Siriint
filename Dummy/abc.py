from common import *

soup = req_bsEncoding('https://bot-hive.com/product/franka-emika-panda')

top_highlight = soup.select('div.tab__content__body__info')
highlight = top_highlight[0].select('div p')

for i in highlight:
    print(i.text)

