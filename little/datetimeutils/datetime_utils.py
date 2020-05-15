# -*- coding: utf-8 -*-
# @Time: 2020/5/14 17:55
import datetime


class DatetimeLittle(object):
    sdf_date = '%Y-%m-%d'
    sdf_datetime = '%Y-%m-%d %H:%M:%S'

    @staticmethod
    def date_increment(base_date=None,offset=1):
        '''
        :param base_date: 计算基数
        :param offset: 时间加减幅度
        :return: 基于base_date计算后的日期YYYY-mm-dd
        '''
        if base_date is None:
            base_date = DatetimeLittle.get_now_date()
        elif len(base_date)>10:
            base_date = base_date[:10]
        dt = datetime.datetime.strptime(base_date, "%Y-%m-%d")
        out_date = (dt + datetime.timedelta(days=offset)).strftime("%Y-%m-%d")
        return out_date

    @staticmethod
    def get_now_date(sdf='%Y-%m-%d'):
        '''
        :param sdf: 需要的日期格式：%Y-%m-%d
        :return: %Y-%m-%d
        '''
        return datetime.datetime.now().strftime(sdf)

    @staticmethod
    def get_now_datetime(sdf='%Y-%m-%d %H:%M:%S'):
        '''
        :param sdf: 需要的时间格式：%Y-%m-%d %H:%M:%S
        :return: %Y-%m-%d %H:%M:%S
        '''
        return datetime.datetime.now().strftime(sdf)


if __name__ == "__main__":
    # print(DatetimeLittle.get_now_date())
    # print(DatetimeLittle.get_now_datetime())
    print(DatetimeLittle.date_increment(DatetimeLittle.get_now_datetime(),-2))