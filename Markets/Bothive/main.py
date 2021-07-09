from common import *
import bothive_configuration.bothive_config as config
from Markets.Bothive.bothive_crawl.bothive_1depth import crawl_key
from Markets.Bothive.bothive_crawl.bothive_2depth import crawl_detail
from Markets.Bothive.bothive_crawl.bothive_transform import trans

def bothive_run(save=True):
    dic_bothive1 = crawl_key(sample=True, save=True)
    dic_bothive2 = crawl_detail(dic_bothive1, save=True)
    json_bothive = trans(dic_bothive2)

    if save == True:
        json_save('./json/bothive_result.json', json_bothive)
    return json_bothive


if __name__ == '__main__':
    bothive_run()