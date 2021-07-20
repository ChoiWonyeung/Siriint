from common import *
import pandas as pd



def json_load(file):
    with open(f'../makeExcel(full_length)/{file}.json') as json_file:
        result = json.load(json_file)
        return result

cobot = json_load('cobot_2depth')
qviro = json_load('qviro_2depth')
thinkbotsolutions = json_load('thinkbotsolutions_2depth')
bothive = json_load('bothive_2depth')
komachine = json_load('komachine_2depth')
daara = json_load('daara_2depth_')

df_cobot = pd.DataFrame(cobot).transpose()
df_qviro = pd.DataFrame(qviro).transpose()
df_thinkbotsolutions = pd.DataFrame(thinkbotsolutions).transpose()
df_bothive = pd.DataFrame(bothive).transpose()
df_komachine = pd.DataFrame(komachine).transpose()
df_daara = pd.DataFrame(daara).transpose()


df_cobot.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/cobot.csv')
df_qviro.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/qviro.csv')
df_thinkbotsolutions.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/thinkbotsolutions.csv')
df_bothive.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/bothive.csv')
df_komachine.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/komachine.csv')
df_daara.to_csv('/Users/kimkangnam/PycharmProjects/CompanyProject/DataVoucher/Bigwave-Robotics/makeExcel(full_length)/daara.csv')