from bs4 import BeautifulSoup
from IO import *
import time
import requests
import pickle
import random
import pandas as pd

dic_unchained = pickle_load('pickle/dic_unchained_1depth.pkl')
ls_source = list(dic_unchained.keys())

def delrn(text):
    return text.replace('\xa0', ' ').replace('"', '').replace("\t", "").replace("\n", "").replace("\r", "").lstrip().rstrip()

def getPost(ls_source) -> list:
    counter = 1
    for post in ls_source:

        url = post
        time.sleep(random.uniform(1,5))
        req = requests.get(post, verify=False)
        soup = BeautifulSoup(req.text, 'html.parser')
        print(str(counter) + '번째 수집중')
        brand = soup.find('p',{'id':'breadcrumbs'}).text
        dic_unchained[post]['Brand'] = brand.split(' → ')[3]
        dic_unchained[post]['Category'] = brand.split(' → ')[2]
        dic_unchained[post]['Product'] = soup.find('div',{'class':'elementor-jet-single-title'}).text
        dic_unchained[post]['Model'] = soup.find('div',{'class':'elementor-jet-single-title'}).text

        dic_unchained[post]['Image'] = []
        for img in soup.findAll('div',{'class':'jet-woo-swiper-control-thumbs__item-image'}):
            try:dic_unchained[post]['Image'].append(img.find('img')["src"])
            except:continue
        try:
            if dic_unchained[post]['Image'] == [] :
                dic_unchained[post]['Image'].append(soup.find('a',{'class':'jet-woo-product-gallery__image-link'})['href'])
        except:
            for img in soup.find('figure',{'class':'woocommerce-product-gallery__wrapper'}).findAll('a'):
                dic_unchained[post]['Image'].append(img['href'])

        try:
            dic_unchained[post]['File'] = soup.find('a',{'class':'uael-infobox-module-link'})['href']
        except:
            dic_unchained[post]['File'] = None
        dic_unchained[post]['Price'] = soup.find('span',{'class':'woocommerce-Price-amount'}).text

        #스펙
        num = 0
        try:
            dic_specout = {}
            lsspec = soup.find('table',{'class':'jet-table--fa5-compat'}).findAll('div',{'class':'jet-table__cell-text'})
            specnum = len(lsspec)
            while True:
                dic_spec = {lsspec[num].text : lsspec[num+1].text}
                dic_specout.update(dic_spec)
                num = num + 2
                if num >= specnum : break
        except:dic_specout = None
        dic_unchained[post]['Specification'] = dic_specout

        dic_unchained[post]['Seller'] = {'Name':'Unchained Robotics', 'Phone':'+49 1522 2798924'}

        try:DesText = delrn(soup.find('div',{'data-elementor-type':'jet-woo-builder'}).findAll('section')[10].text)
        except:DesText = None
        DesImage = []
        try:
            for img in soup.find('div',{'data-elementor-type':'jet-woo-builder'}).findAll('section')[10].findAll('img'):
                DesImage.append(img['src'])
        except:DesText = None
        try:dic_unchained[post]['Description'] = {'Text':DesText, 'Image':DesImage}
        except:
            try:dic_unchained[post]['Description'] = {'Image':DesImage}
            except:
                try:dic_unchained[post]['Description'] = {'Text':DesText}
                except:dic_unchained[post]['Description'] = None

        dic_unchained[post]['Url'] = url
        print(dic_unchained[post])
        counter = counter + 1

    pickle_save('pickle/dic_unchained_2depth.pkl', dic_unchained)
    pd.DataFrame(dic_unchained).to_csv("data/unchained.csv",encoding='utf-8-sig')
    json_save("data/unchained.json", dic_unchained)

getPost(ls_source)