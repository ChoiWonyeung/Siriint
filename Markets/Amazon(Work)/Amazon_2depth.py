from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Pickle import *
import pandas as pd
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
    counter = 0
    for post in ls_source:
        counter = counter + 1
        print(str(counter)+'번째 수집중')
        url = post
        driver.get(post)
        time.sleep(1)
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')

        #브랜드명 적재 없을시 None
        lsbrand = soup.find('div',{'id':'productOverview_feature_div'}).findAll('td')
        brandnum = 0
        for brand in lsbrand :
            try:
                if 'Brand' in lsbrand[brandnum].text:
                    dic_amazon[post]['Brand'] = delrn(lsbrand[brandnum+1].text)
                    break
                else: dic_amazon[post]['Brand'] = None
            except:
                dic_amazon[post]['Brand'] = None
                break
            brandnum = brandnum + 2

        #프로덕트 적재
        dic_amazon[post]['Product'] = delrn(soup.find('span',{'id':'productTitle'}).text)

        #모델명 적재 없을시 None
        brandnum = 0
        for brand in lsbrand :
            try:
                if 'Model' in lsbrand[brandnum].text:
                    dic_amazon[post]['Model'] = delrn(lsbrand[brandnum+1].text)
                    break
                else: dic_amazon[post]['Model'] = None
            except:
                dic_amazon[post]['Model'] = None
                break
            brandnum = brandnum + 2

        # 이미지 미리보기 갯수, 태그 찾기
        imageclick = soup.findAll('li',{'class':'a-declarative'})
        imagenum = int(soup.find('li', {'class': 'a-declarative'}).find('span',{'class':'a-button-thumbnail'})['id'][-1])

        #이미지 미리보기 갯수만큼 반복하여 이미지 활성화
        for clicked in imageclick:
            clickpoint = driver.find_element_by_id('a-autoid-'+str(imagenum))
            ActionChains(driver).move_to_element(clickpoint).perform()
            imagenum=imagenum+1
        #이미지 활성화 후 소스 재지정
        source = driver.page_source
        soup = BeautifulSoup(source, 'html.parser')
        dic_amazon[post]['Image'] = []
        #이미지 수집
        for img in soup.findAll('div',{'class':'imgTagWrapper'}):
            try:dic_amazon[post]['Image'].append(img.find('img')["src"])
            except:continue
        #동영상 수집
        try:
            dic_amazon[post]['Video'] =soup.find('div',{'class':'airy-renderer-container'}).find('video')['src']
        except:
            dic_amazon[post]['Video'] = None

        dic_amazon[post]['Files'] =None

        dic_amazon[post]['Option'] =None

        #가격 수집 할인이 될 경우 할인전 가격/할인되는 가격/할인 후 가격 으로 표기
        try:
            listprice = delrn(soup.find('span', {'class': 'priceBlockStrikePriceString'}).text)
            saveprice = delrn(soup.find('td', {'class': 'priceBlockSavingsString'}).text)
        except:
            listprice=None
            saveprice=None
        try:
            Price = soup.find('span', {'id':'priceblock_ourprice'}).text.replace(' ', '')
        except:
            try:
                Price = soup.find('span', {'id': 'priceblock_dealprice'}).text
            except:
                Price = soup.find('span', {'id': 'priceblock_saleprice'}).text
                try:Price = '품절'
        try:
            dic_amazon[post]['Price'] = listprice+"/"+saveprice+"/"+Price
        except:
            dic_amazon[post]['Price'] = Price

        #워런티가 비어있는 경우 데이터는 None으로 적재
        try:
            dic_amazon[post]['Warranty'] =delrn(soup.find('div', {'id':'prodDetails'}).find('div', {'class':'a-span-last'}).find('div', {'class':'a-section'}).text).replace('Product Warranty: ', '')
        except:
            dic_amazon[post]['Warranty'] = None

        if '품절' in Price :
            dic_amazon[post]['Shipping'] = '품절로 인해 배송 불가'
        else : dic_amazon[post]['Shipping'] = soup.find('span', {'id':'tabular-buybox-truncate-0'}).text

        if '품절' in Price :
            dic_amazon[post]['ShippingDate'] = '품절로 인해 배송 불가'
        else : dic_amazon[post]['ShippingDate'] = None
        dic_amazon[post]['Specification'] = None

        #패키징 적재 없을시 None
        brandnum = 0
        for brand in lsbrand:
            try:
                if 'Dimensions' in lsbrand[brandnum].text:
                    dic_amazon[post]['Package'] = delrn(lsbrand[brandnum+1].text)
                    break
                else: dic_amazon[post]['Package'] = None
            except:
                dic_amazon[post]['Package'] = None
                break
            brandnum = brandnum + 2


        #판매자 적재
        try:
            dic_amazon[post]['Seller'] = soup.find('a',{'id':'sellerProfileTriggerId'}).text
        except:
            if '품절' in Price :
                dic_amazon[post]['Seller'] = '품절로 인해 판매자 없음'
            else : dic_amazon[post]['Seller'] = 'Amazon.com'

        #인포메이션 적재
        try:
            information = soup.find('table',{'id':'productDetails_detailBullets_sections1'}).findAll('tr')
            dic_amazon[post]['Information'] = []
            for infor in information:
                inforout = {delrn(infor.find('th').text) : delrn(infor.find('td').text)}
                dic_amazon[post]['Information'].append(inforout)
        except:
            dic_amazon[post]['Information'] = None

        #상품정보 적재
        try:
            DesText = delrn(soup.find('div',{'data-cel-widget':'aplus'}).text)
        except:DesText = None
        DesImage = []
        try:
            for img in soup.find('div',{'data-cel-widget':'aplus'}).findAll('img'):
                if 'grey-pixel' in img['src']:continue
                DesImage.append(img['src'])
        except:DesText = None
        dic_amazon[post]['Description'] = {'Text':DesText, 'Image':DesImage}

        #상품 Url 적재
        dic_amazon[post]['Url'] = url

        print(dic_amazon[post])
    pd.DataFrame(dic_amazon).to_csv("data/"+ 'amazon' + ".csv",encoding='utf-8-sig')
getPost()