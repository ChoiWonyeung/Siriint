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
selector_image = 'div.detailTopImg > img'

dic_selector = {'catlog': selector_catalog,
                'type1': selector_type1,
                'type2': selector_type2,
                'description1': selector_description1,
                'description2': selector_description2,
                'delivery': selector_delivery,
                'image': selector_image}