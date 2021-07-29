from bs4 import BeautifulSoup
from IO import *
import time
import requests
import pickle


def getList() -> list:
    ###
    dic_unchaineds = []#Url을 담을 리스트
    url = 'https://unchainedrobotics.de/en/marketplace/?compare=2789,6722'
    '''
     --- 1페이지부터 <사이트마다 page 파라미터 확인>
    '''
    req = requests.get(url, verify=False)
    soup = BeautifulSoup(req.text, 'html.parser')

    pages = soup.find('div',{'class':'jet-woo-products'}).findAll('div',{'class':'jet-woo-products__item'})
    for url in pages:

        postInfor = {
            'url': url.find('a')['href']
        }
        # 수집되지 않은 url이면 append
        exist = next((item for item in dic_unchaineds if item['url'] == postInfor['url']), None)
        if type(exist) != dict:
            dic_unchaineds.append(postInfor)
        else:
            break

    dic_unchained = {}
    for urls in dic_unchaineds:
        dic_unchained[urls['url']]={}

    print(dic_unchained)
    #수집된 데이터를 pickle로 저장
    pickle_save('pickle/dic_unchained_1depth.pkl', dic_unchained)

    with open('pickle/dic_unchained_1depth.pkl', 'rb') as f:
        obj = pickle.load(f)

getList()