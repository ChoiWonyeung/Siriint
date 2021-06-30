# 페이지 url (페이지 넘버 없음)
url_page = 'https://www.komachine.com/ko/categories/fa-factory-automation/?type=product&page='

# 1차 크롤링 셀렉터
selector_product = '.model'
selector_title = 'p.title'
selector_series = 'p.series'
selector_source = 'a.item.product'

# 2차 크롤링 셀렉터
selector_image = 'button.wrapper.img'
selector_catalog = 'section.product-info > div.product-doc > table > tbody'
selector_description = 'section.content-main > section.product-desc.fr-view'
