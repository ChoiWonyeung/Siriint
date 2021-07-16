import os

# url 정보
url_product = 'https:///bot-hive.com/products'

# 1차 크롤링
selector_image = '.product-tile__image > img'
selector_brand = ".colour--carmine"
selector_type1 = '.product-tile__details__detail.colour--mountbattenPink'
selector_product = '.colour--jacaranda'

# 버튼
selector_button = 'body > app-root > div > main > div > app-products > div > div > div > button'

# 2차 크롤링
selector_source = '.product-tile'
selector_highlight = 'div.tab__content__body__info' #highlight
selector_description = '.tab__description'
selector_spec = '.tab__key-info__info'
selector_delivery = '.text--weight-bold.text--16.ng-star-inserted'

#
path_pickles = os.path.abspath("../pickles")
path_json = ('../json')