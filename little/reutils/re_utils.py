# -*- coding: utf-8 -*-
# @Time: 2020/5/14 17:57
import re


class ReLittle(object):

    digital_pattern = re.compile(r"\d+")

    @staticmethod
    def extract_digital_2_str(content):
        '''

        :param content:
        :return: 字符串型的列表
        '''
        results = re.findall(ReLittle.digital_pattern,content)
        return results

    @staticmethod
    def extract_digital_2_int(content):
        '''

        :param content:
        :return: 整型的列表
        '''
        results = re.findall(ReLittle.digital_pattern, content)
        results = [int(s) for s in results]
        return results

if __name__ == "__main__":
    print(ReLittle.extract_digital_2_int("dds23dd4sd23"))

