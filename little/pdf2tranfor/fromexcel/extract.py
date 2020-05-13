# _*_ coding:utf-8 _*_
# @Time 2020/5/12 9:49 下午
import pandas


class Extract(object):

    def run(self):
        filename = '117-158.xlsx'
        year = 2019
        level = "本科一批"
        face_pro = "重庆"
        student_type = "文科"

        columns = ["college_no","college","major","enrollment","min",'max']
        pd_obj = None
        for pd in self.extract_data(filename, columns):
            pd['year'] = year
            pd['level'] = level
            pd['face_pro'] = face_pro
            pd['student_type'] = student_type
            if pd_obj is None:
                pd_obj = pd
            else:
                pd_obj = pd_obj.append(pd)
        pd_obj.to_csv(filename+".csv",mode='a',index=False)

    def extract_data(self, filename, columns):

        xl = pandas.ExcelFile(filename)
        sheet_names = xl.sheet_names
        for sheet_name in sheet_names:
            pd = pandas.read_excel(filename,sheet_name=sheet_name,header=2,dtype=str)
            pd = self.fix_pad(pd,columns)
            yield pd

    def fix_pad(self,pd,columns):
        pd.columns = columns
        pd = pd.fillna(method='pad')
        pd.drop_duplicates(ignore_index=False,inplace=True,keep="first",subset=["college","major"])
        # 数据清理
        pd = self.clear_data(pd)

        return pd

    def clear_data(self,pd):
        pd['major'] = pd['major'].str.strip("1")
        pd = pd.applymap(lambda x: x.strip("！£!’'、‘•\"|,■.「:@，/一：_；「…- \\"))
        pd = pd.applymap(lambda x: x[2:] if x.startswith("0.") else x)
        return pd
    # def clear_digital(self,):


if __name__ == "__main__":
    Extract().run()
    s = "0.223"
    s = s[2:] if s.startswith("0.") else s
    print(s)