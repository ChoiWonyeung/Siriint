import komachine_1depth
import komachine_2depth
import komachine_transform

def main():
    dic_komachine1 = komachine_1depth.crawl_key(sample=True)
    dic_komachine = komachine_2depth.crawl_detail(dic_komachine1)
    json_komachine = komachine_transform.transformation(dic_komachine)
    return json_komachine

if __name__ == '__main__':
    dic_komachine = main()