# url
url = 'https://thinkbotsolutions.com/collections/all'
url_noNumber = 'https://thinkbotsolutions.com/collections/all?page=' # url 상품 페이지 넘버링 제거

# 1차 크롤링 셀렉터
selector_company = '.product-item__vendor.link'
selector_product = '.product-item__title.text--strong.link'
selector_source = '.product-item__title.text--strong.link' #href
selector_price = '.product-item__price-list'

#차 크롤링 셀렉터
selector_image = '.product-gallery__thumbnail-list img'
selector_sku = '.product_meta__sku'
selector_description = '.product-block-list__item--description'
selector_specifications = '.product-block-list__item--content'
selector_video = '.video-wrapper > iframe'
