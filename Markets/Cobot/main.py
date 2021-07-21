from Markets.Cobot.crawl.cobot_1depth import crawl_key
from Markets.Cobot.crawl.cobot_2depth import crawl_detail
from Markets.Cobot.crawl.cobot_transform import transform


def main():
    dic_cobot1 = crawl_key(sample=False, save=False)
    dic_cobot2 = crawl_detail(dic_cobot1, save=True)
    # json_cobot = transform(dic_cobot)
    # json_save('./json/cobot_result.json', json_cobot)


if __name__ == '__main__':
    main()