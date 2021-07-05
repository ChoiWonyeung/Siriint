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
selector_highlight = '.tab__content__body' #highlight
selector_description1 = '.tab__description'
selector_description2 = ''
selector_spec = '.tab__key-info__info p'
selector_delivery = '.text--weight-bold.text--16.ng-star-inserted'


#
path_pickle = '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Bothive/bothive_pickle/'