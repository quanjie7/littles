#-*- coding: utf-8 -*-

class Str2Map(object):

    @staticmethod
    def cookie_str_2_map(content,split=";"):
        str_array = content.split(split)
        res = {}
        if str_array:
            for item_str in str_array:
                item_str = item_str.strip()
                kv = item_str.split("=")
                k = kv[0]
                v = kv[1]
                res[k] = v

        return res


if __name__ == "__main__":
    str1 = "53revisit=1591177347389; sid=ebc8775a4e4b1ab099d117d9bb51e179; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22182875%22%2C%22%24device_id%22%3A%22172798f7f382ee-0a4abeb401c5eb-6e52712d-2073600-172798f7f39423%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22172798f7f382ee-0a4abeb401c5eb-6e52712d-2073600-172798f7f39423%22%7D; _lssk_=1%2C2; route=ac64594b752ca56e53f3e1170d443cdd; 53kf_72209196_from_host=www.sieredu.com; 53kf_72209196_keyword=; 53kf_72209196_land_page=https%253A%252F%252Fwww.sieredu.com%252Fweb%252Fexam%252Findex%252FexamIndex; kf_72209196_land_page_ok=1"
    res = Str2Map.cookie_str_2_map(str1)
    print(res)
