

for url2 in sample_source:
    dic_robotshop[url2] = {}
    sel_bsEncoding(url2)
    sleep_random(2, 4)
    div_product = driver.find_elements_by_css_selector('div.product-col-box')

    # image
    div_image = div_product[0].find_elements_by_css_selector('div.product-image')
    image_ls = div_image[0].find_elements_by_css_selector('div.slick-slide > div > div > img')
    image = [i.get_attribute('src') for i in image_ls]


