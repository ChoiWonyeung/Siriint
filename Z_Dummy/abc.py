from common import *
import pandas as pd



def json_load(file):
    with open(f'../makeExcel/{file}.json') as json_file:
        result = json.load(json_file)
        return result

cobot = json_load('cobot_2depth')
qviro = json_load('qviro_2depth')
thinkbotsolutions = json_load('thinkbotsolutions_2depth')

df_cobot = pd.DataFrame(cobot).transpose()
df_qviro = pd.DataFrame(qviro).transpose()
df_thinkbotsolutions = pd.DataFrame(thinkbotsolutions).transpose()

df_cobot.to_csv('./cobot.csv')
df_qviro.to_csv('./qviro.csv')
df_thinkbotsolutions.to_csv('./thinkbotsolutions.csv')