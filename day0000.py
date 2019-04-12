#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 15:15
# @Author  : hahaya
# @Site    : 
# @File    : day0000.py
# @Software: PyCharm


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os


def addnum(img):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    # 右上角加数字
    myfont = ImageFont.truetype(os.getcwd() + '\\font.ttf', size=40)
    filcolor = '#ff0000'
    draw.text((width - 50, 0), '99', font=myfont, fill=filcolor)
    img.save(os.getcwd() +'\\result.jpg', 'jpeg')


if __name__ == '__main__':
    img = Image.open(os.getcwd() + "\\test.png")
    addnum(img)
