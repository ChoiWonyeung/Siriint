from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pickle import *

import time


def delrn(text):
    return text.replace('"','').replace('"','').replace("\t", "").replace("\n", "").replace("\r", "").lstrip().rstrip()
def getPost() -> list:
    options = Options()
    #options.add_argument('headless')  # disable-gpu와 같이 사용. 크롬 드라이버의 표시를 막아줌(리소스 최적화 및 속도 향상)
    #options.add_argument("disable-gpu")
    #options.add_argument('window-size=1920x1080')  # 크롬 드라이버 화면 사이즈 지정
    driver = webdriver.Chrome('chromedriver', chrome_options=options)  # 크롬드라이버 실행
    Urls = pickle_load('pickle/dic_amazon_1depth.pkl')
    #####
    for post in Urls:
        url = post
        driver.get(post)
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        print(delrn(soup.find('span',{'id':'productTitle'}).text))
        #post['Brand'] =
        post['Product']= delrn(soup.find('span',{'id':'productTitle'}).text)
        #post['Model'] =
        post['Image'] = []
        for img in soup.findAll('div',{'class':'imgTagWrapper'}):
            post['Image'].append(img['src'])
        post['Video'] =soup.find('div',{'class':'airy-renderer-container'}).find('video')['src']
        #post['Files'] =
        #post['Option'] =
        post['Price'] =soup.find('span',{'id':'priceblcok_ourprice'}).text
        post['Warranty'] =delrn(soup.find('span',{'class':'table-padding'}).text).replace('Product Warranty:','')
        #post['Shipping'] =
        #post['ShippingDate'] =
        #post['Specification'] =
        #post['Package'] =
        #post['Order'] =
        #post['Seller'] =
        #post['Information'] =
        #post['Description'] =
        post['Url'] =url

        print(post)
        break

getPost()