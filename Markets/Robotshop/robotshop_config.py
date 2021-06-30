# url
dic_url = {0: 'https://www.robotshop.com/en/robots-to-build.html?p=',
           1: 'https://www.robotshop.com/en/robots-for-the-house.html?p=',
           2: 'https://www.robotshop.com/en/robot-toys.html?p=',
           3: 'https://www.robotshop.com/en/professional-service-robots.html?p=',
           4: 'https://www.robotshop.com/en/industrial-robotics.html?p=',
           5: 'https://www.robotshop.com/en/wearable-technology.html?p='}

#1차 크롤링 셀렉터
selector_source = '.product-name > a'

#2차 크롤링 셀렉터
selector_image = 'img.big-image'
selector_brand = '.brandLogoBox > a'
selector_product = '.product-info-section .product-title'
selector_price = '.regular-price .price'
selector_highlights = 'section.product-short-desc'  # description1
selector_description = '.aboutBox.BoxDescription.product-sheet-attribute'  # description2
selector_spec = '.product-sheet-attribute.aboutBox.Specifications'  # spec
selector_model = '#Supplier-Product-Code'  # 'model' or 'supplier product code'
selector_dimension = '.product-sheet-attribute.aboutBox.Dimensions'  # size
selector_catalog = '.aboutContent.clearfix > ul > li > a'  # href

dic_selector = {'image': selector_image,
                'product': selector_product,
                'price': selector_price,
                'brand': selector_brand,
                'highlight': selector_highlights,
                'description1': selector_description,
                'spec': selector_spec,
                'model': selector_model,
                'dimension': selector_dimension,
                'catalog': selector_catalog}
