from thinkbotsolutions_1depth import crawl_key
from thinkbotsolutions_2depth import crawl_detail

if __name__ == '__main__':
    dic_thinkbotsolution = crawl_key(save=True)
    dic_thinkbotsolution1 = crawl_detail(dic_thinkbotsolution, save=True)