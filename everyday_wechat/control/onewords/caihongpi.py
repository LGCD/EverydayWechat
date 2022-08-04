# -*- coding=utf-8 -*-

"""
https://chp.shadiao.app/?from_nmsl
彩虹屁生成器
 """
import json

import requests

__all__ = ['get_caihongpi_info']


def get_caihongpi_info():
    """
    彩虹屁生成器
    :return: str,彩虹屁
    """
    print('获取彩虹屁信息...')
    try:
        resp = requests.get('https://api.shadiao.pro/chp')
        if resp.status_code == 200:
            return json.loads(resp.text)["data"]["text"]
        print('彩虹屁获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    # return None


get_one_words = get_caihongpi_info

if __name__ == '__main__':
    ow = get_one_words()
    print(ow)
    pass
