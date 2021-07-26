from Modules.common import *
import configuration.bothive_config as config
from Markets.Bothive.python.bothive_1depth import crawl_key
from Markets.Bothive.python.bothive_2depth import crawl_detail
from Markets.Bothive.python.bothive_transform import transformation

def main(save=False, sample=False, headless=False):
    dic_bothive1 = crawl_key(save=False, sample=False, headless=True)
    dic_bothive2 = crawl_detail(dic_bothive1, save=False)
    json_bothive = transformation(dic_bothive2)
    return json_bothive


if __name__ == '__main__':
    main()