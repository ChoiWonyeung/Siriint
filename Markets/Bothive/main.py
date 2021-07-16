from common import *
import configuration.bothive_config as config
from Markets.Bothive.python.bothive_1depth import crawl_key
from Markets.Bothive.python.bothive_2depth import crawl_detail
from Markets.Bothive.python.bothive_transform import transformation

def main(save=True, sample=False):
    dic_bothive1 = crawl_key(save, sample)
    dic_bothive2 = crawl_detail(dic_bothive1, save)
    json_bothive = transformation(dic_bothive2)

    return json_bothive


if __name__ == '__main__':
    main()