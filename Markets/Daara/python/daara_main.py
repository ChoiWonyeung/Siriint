import json
from common import *
from Markets.Daara.python.daara_1depth import crawl_key
from Markets.Daara.python.daara_2depth import crawl_detail
from Markets.Daara.python.daara_transform import transformation

def main(save=True, sample=False):
    depth1 = crawl_key(save, sample)
    depth2 = crawl_detail(depth1, save)
    json_daara = transformation(depth2, save)



if __name__ == "__main__":
    main(save=True)