import os
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
import unicodedata
from selenium import webdriver
import pickle
import json


path_webdriver = '/Users/kimkangnam/Desktop/Chromedriver/chromedriver'

#################################################


def pickle_save(file, obj):
    with open(file, 'wb') as f:
        pickle.dump(obj, f)


def pickle_load(file):
    with open(file, 'rb') as f:
        obj = pickle.load(f)
        return obj


def json_save(file, object):
    with open(file, 'w', encoding='utf-8') as file_json:
        json.dump(object, file_json, indent='\t', ensure_ascii=False)


def get_webdriver(path_webdriver, wait_time = 10):
    """
    :param path_webdriver:
    :param wait_time:
    :return:
    """
    global driver
    driver = webdriver.Chrome(path_webdriver)
    driver.implicitly_wait(wait_time)
    return driver


def req_bsEncoding(url):
    """
    return beautifulSoup encoding result.
    for request library
    :param url:
    :return: soup = BeautifulSoup(html, 'html.parser)
    """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def check_ip():
    """
    IP address check.
    return result does NOT provide print function by own.
    :return: request.text
    """
    url = 'http://icanhazip.com/'
    res = requests.get(url)
    print(res)
    result = res.text
    print(res.text)
    return result


def check_response(url):
    """
    Check requests module response
    :param url:
    :return: requests.get(url)
    """
    res = requests.get(url)
    result = res.ok
    print(res)
    return result


def sleep_random(start_second=2, end_second=10, print_time=False):
    """
    2~10초 사이의 랜덤 sleep
    :param start_second: default = 2 s
    :param end_second:   default = 10 s
    :param print_time:   default = False
    :return:
    """
    random_seconds = random.uniform(start_second, end_second)
    time_sleep = time.sleep(random_seconds)
    if print_time is True:
        print(f'Random sleep seconds :{random_seconds}')
    return time_sleep


def df_bigWaveRobotics():
    """
    :return: DataFrame
    """
    Columns = ['No',
               'brand',
               'type1',
               'type2',
               'product',
               'model',
               'price',
               'highlight',
               'image',
               'video',
               'catalog',
               'option',
               'description1',
               'description2',
               'spec',
               'delivery',
               'order',
               'seller',
               'source',
               'source_name']
    df = pd.DataFrame(columns=Columns)
    return df


def dic_bigWaveRobotics(result=''):
    result = {
        'brand': [],
        'type1': [],
        'type2': [],
        'product': [],
        'model': [],
        'price': [],
        'highlight': [],
        'image': [],
        'video': [],
        'catalog': [],
        'option': [],
        'description1': [],
        'description2': [],
        'spec': [],
        'delivery': [],
        'order': [],
        'seller': []}
    return result


def sel_bsEncoding(url):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def driverText(selector, toList=True):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.text for element in elements]
    if toList is True:
        return result
    elif toList is False:
        for i in range(len(result)):
            return result[i]


def ls_driverFinder(selector, key):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.get_attribute(key) for element in elements]
    return result


def ls_driverHref(selector):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.get_attribute('href') for element in elements]
    return result


def ls_driverSrc(selector):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.get_attribute('src') for element in elements]
    return result


def ls_driverStyle(selector):
    elements = driver.find_elements_by_css_selector(selector)
    result = [element.get_attribute('style') for element in elements]
    return result


def textmake(soup, selector):
    ls = []
    for text_soup in soup.select(selector):
        ls.append(text_soup.text)
    return ls


def ls_hrefmake(soup, selector, str_add=''):  # href->리스트 반환 함수
    ls_href = []
    for href_soup in soup.select(selector):
        ls_href.append(str_add + href_soup['href'])
    return ls_href


def ls_srcmake(soup, selector, str_add=''):
    ls_src = []
    for src_soup in soup.select(selector):
        ls_src.append(str_add + src_soup['src'])
    return ls_src


# def numbering_duplicatedFile(save_path, save_file, save_ext):
#     unique_number = 1
#     while os.path.exists(save_path):
#         result = '/%s%(%d)%(%s)' % (file_name, unique_number, file_ext)
#         unique_number += 1