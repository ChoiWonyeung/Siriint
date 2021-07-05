# url
url_page = 'http://mall.daara.co.kr/product/list.html?cd=103100&page='

# 1차 크롤링
selector_product = '.name > a'
selector_source = '.bbsSubFixed > div > a'
selector_brand = '.brand > a'
selector_price = '.price_box > p.btn_estimate'

# 2차 크롤링
selector_type1 = '.category2 > a'
selector_type2 = '.on.category3 > a'
selector_catalog = '.btn-down'
selector_highlight = '.goodsDetail > li'
selector_order = '.num_dc > li'
selector_seller = '.common-row-table.prdc-detail'
selector_description1 = '.table thead'
selector_description2 = '.table tbody'
selector_delivery = '.common-rw-table.prdc-detail span'

# 2차 - 이미지
# image_start = 'pimg.daara.co.kr/mall/photo'
# image_format = 'png', 'jpg', ''

selector_image = 'div.detailTopImg > img'

# 셀렉터 항목 딕셔너리 화
dic_selector = {
    'type1': selector_type1,
    'type2': selector_type2,
    'catalog': selector_catalog,
    'highlight': selector_highlight,
    'order': selector_order,
    'seller': selector_seller,
    'description1': selector_description1,
    'description2': selector_description2,
    'delivery': selector_delivery,
    'image': selector_image
}

# 경로
path_pickle = '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Daara/daara_pickles/'
path_dataResult = '/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/Markets/Daara/daara_dataResults/'