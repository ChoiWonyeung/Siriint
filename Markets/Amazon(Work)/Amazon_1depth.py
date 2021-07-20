import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pickle import *



#아마존은 쿠키를 체크해 봇을 차단하여 리퀘스트 사용이 불가능함에 따라 셀레니움으로 진행하였습니다.
def getList() -> list:
    ###
    dic_amazons = []#Url을 담을 리스트
    url = 'https://www.amazon.com/s?k=robot&i=toys-and-games&rh=n%3A343404011&dc&page={page}&qid=1626742020&rnid=2941120011&ref=sr_pg_2'#페이지 부분에 포멧 설정
    '''
     --- 1페이지부터 <사이트마다 page 파라미터 확인>
    '''
    options = Options()
    options.add_argument('headless')  # disable-gpu와 같이 사용. 크롬 드라이버의 표시를 막아줌(리소스 최적화 및 속도 향상)
    options.add_argument("disable-gpu")
    options.add_argument('window-size=1920x1080')  # 크롬 드라이버 화면 사이즈 지정
    driver = webdriver.Chrome('chromedriver', chrome_options=options)  # 크롬드라이버 실행

    driver.get(url.format(page = 1))#해당 상품리스트의 첫 페이지로 접속
    time.sleep(1)#로딩시간 고려 1초간 대기
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    # --- 마지막페이지 확인
    lastpager = soup.find('ul', {'class': 'a-pagination'})#해당 상품리스트의 마지막 페이지 체크
    if lastpager.findAll('li') :#마지막 페이지 부분이 존재한다면 마지막 페이지 설정
        lastPage = int(
            lastpager.findAll('li')[-2].text)
    else:#마지막 페이지 부분이 존재하지 않는다면 마지막 페이지를 1로 설정
        lastPage = 1
    print(lastPage)

    # 첫페이지부터 마지막페이지까지
    for page in range(1, lastPage + 1):
        driver.get(url.format(page=page))
        source = driver.page_source
        print('[ * ] page -> ' + str(page))
        soup = BeautifulSoup(source, 'html.parser')

        # 게시물 리스트 url 수집
        for a in soup.findAll('span',{'class':'template=SEARCH_RESULTS'}):
            postInfor = {
                'url': 'https://www.amazon.com/'+a.find('a',{'class':'a-link-normal'})['href']
            }
            # 수집되지 않은 url이면 append
            exist = next((item for item in dic_amazons if item['url'] == postInfor['url']), None)
            if type(exist) != dict:
                dic_amazons.append(postInfor)
            else:
                break
    pickle_save('pickle/dic_amazon_1depthtest.pkl', dic_amazons)

    dic_amazon={}
    for urls in dic_amazons:
        dic_amazon[urls['url']]={}


    #수집된 데이터를 pickle로 저장
    pickle_save('pickle/dic_amazon_1depth.pkl', dic_amazon)

    A = pickle_load('pickle/dic_amazon_1depth.pkl')
getList()