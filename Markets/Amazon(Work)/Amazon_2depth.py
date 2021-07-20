from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from Pickle import *

import time


def delrn(text):
    return text.replace('"','').replace('"','').replace("\t", "").replace("\n", "").replace("\r", "").lstrip().rstrip()
def getPost() -> list:
    options = Options()
    #options.add_argument('headless')  # disable-gpu와 같이 사용. 크롬 드라이버의 표시를 막아줌(리소스 최적화 및 속도 향상)
    #options.add_argument("disable-gpu")
    #options.add_argument('window-size=1920x1080')  # 크롬 드라이버 화면 사이즈 지정
    driver = webdriver.Chrome('D:/Utility/chromedriver', chrome_options=options)  # 크롬드라이버 실행
    dic_amazon = pickle_load('pickle/dic_amazon_1depth.pkl')
    ls_source = list(dic_amazon.keys())
    #####
    for post in ls_source:
        url = post
        driver.get(post)
        time.sleep(1)
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        print(soup.find('div',{'id':'altImages'}))
        imageclick = soup.find('div',{'id':'altImages'}).findAll('li')
        clicker = 1
        for clicked in imageclick:
            print(clicker)
            driver.find_element_by_xpath('//*[@id="altImages"]/ul/li['+str(clicker)+']').click()
            clicker=clicker+1

        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        #dic_amazon[post]['Brand'] =
        dic_amazon[post]['Product'] = delrn(soup.find('span',{'id':'productTitle'}).text)
        #dic_amazon[post]['Model'] =
        dic_amazon[post]['Image'] = []
        print(soup.findAll('div',{'class':'imgTagWrapper'}))
        for img in soup.findAll('div',{'class':'imgTagWrapper'}):
            print(img)
            print(img['src'])
            dic_amazon[post]['Image'].append(img['src'])
        dic_amazon[post]['Video'] =soup.find('div',{'class':'airy-renderer-container'}).find('video')['src']
        #dic_amazon[post]['Files'] =
        #dic_amazon[post]['Option'] =
        dic_amazon[post]['Price'] =soup.find('span',{'id':'priceblcok_ourprice'}).text
        dic_amazon[post]['Warranty'] =delrn(soup.find('span',{'class':'table-padding'}).text).replace('Product Warranty:','')
        #post['Shipping'] =
        #post['ShippingDate'] =
        #post['Specification'] =
        #post['Package'] =
        #post['Order'] =
        #post['Seller'] =
        #post['Information'] =
        #post['Description'] =
        dic_amazon[post]['Url'] =url

        print(dic_amazon)
        break

getPost()