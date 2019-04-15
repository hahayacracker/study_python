#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 20:36
# @Author  : hahaya
# @Site    : 
# @File    : day0001.py
# @Software: PyCharm
# @Note    : 为你的应用生成激活码（或者优惠券）

import random
str_select = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate(count, length):
    for x in range(count):
        code = ''
        for y in range(length):
            code += random.choice(str_select)
        print(code)


if __name__=='__main__':
    generate(200,20)