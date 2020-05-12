# _*_ coding:utf-8 _*_
# @Time 2020/5/12 9:49 下午
import pandas


class Extract(object):

    def run(self):
        filename = '117-158.xlsx'
        count_sheet = 1
        xl = pandas.ExcelFile(filename)

        sheet_names = xl.sheet_names
        for sheet_name in sheet_names:

            pd = pandas.read_excel(filename,sheet_name=sheet_name,header=2,dtype=str)
            pd = self.fix_pad(pd)
            print(sheet_name,pd)
            print()

    def fix_pad(self,pd):
        pd.columns = ["college_no","college","major","enrollment","min",'max']
        pd = pd.fillna(method='pad')
        pd.drop_duplicates(ignore_index=False,inplace=True,keep="first",subset=["college","major"])
        return pd

if __name__ == "__main__":
    Extract().run()