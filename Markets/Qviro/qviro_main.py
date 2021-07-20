from qviro_crawl.qviro_1depth import crawl_json
from qviro_crawl.qviro_2depth import crawl_detail
from qviro_crawl.qviro_transform import trans
from common import *

def qviro_run(sample=False, save=False):
    dic_qviro = crawl_json(sample, save)
    dic_qviro1 = crawl_detail(dic_qviro, save)
    json_qviro = trans(dic_qviro1)

    if save:
        json_save('../json/qviro_result.json', json_qviro)

    return json_qviro

if __name__ == '__main__':
    qviro_run(sample=False, save=True)