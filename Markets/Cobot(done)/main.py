from Markets.Cobot.crawl.cobot_1depth import crawl_key
from Markets.Cobot.crawl.cobot_2depth import crawl_detail
from Markets.Cobot.crawl.cobot_transform import transform
from common import *


def cobot_run():
    dic_cobot = crawl_key(sample=False, save=True)
    dic_cobot = crawl_detail(dic_cobot, save=True)
    json_cobot = transform(dic_cobot)

    json_save('./json/cobot_result.json', json_cobot)
    return json_cobot


if __name__ == '__main__':
    cobot_run()