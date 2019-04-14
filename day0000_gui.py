#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 10:07
# @Author  : hahaya
# @Site    : 
# @File    : day0000_gui.py
# @Software: PyCharm
# @Note    : GUI版本

import PIL
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageDraw, ImageFont,ImageTk
from tkinter import *
import os


img = None


def select_pic():
    file_path = tkinter.filedialog.askopenfilename(title='选择一张图片', filetypes=[('png','*.png'),('jpg','*.jpg'),('ico','*.ico')])
    #根据文件路径获取文件名
    #file=os.path.basename(file_path)
    #tk的Lable默认只能价值gif格式的图片 所以需要PIL库进行转换
    #PIL和Tk中都有Image 所以前面加PIL表示调用PIL中的
    global img
    img = PIL.Image.open(file_path)
    photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开

    pic_label.config(image=photo,compound = 'center')
    #必须加上先的设置否则图片不显示 参考https://stackoverflow.com/questions/14291434/how-to-update-image-in-tkinter-label
    pic_label.image=photo
    #重新设置Label宽度和高度
    pic_label['width']=600
    pic_label['height'] = 300


def add_num():
    if img==None:
        tkinter.messagebox.showerror('提示','请先选择需要需要添加数字的图片', )
        return
    text = num_text.get('0.0','end')
    print("text:", text)
    if text=="":
        tkinter.messagebox.showerror('提示', '请先输入需要添加的内容', )
        return
    draw = ImageDraw.Draw(img)
    width, height = img.size
    # 右上角加数字
    myfont = ImageFont.truetype(os.getcwd() + '\\font.ttf', size=40)
    filcolor = '#ff0000'
    draw.text((width - 50, 0), text, font=myfont, fill=filcolor)

    photo = ImageTk.PhotoImage(img)
    pic_label.config(image=photo,compound = 'center')
    #必须加上先的设置否则图片不显示 参考https://stackoverflow.com/questions/14291434/how-to-update-image-in-tkinter-label
    pic_label.image=photo
    #重新设置Label宽度和高度
    pic_label['width']=600
    pic_label['height'] = 300


def save_pic():
    name = tkinter.filedialog.asksaveasfilename(filetypes=[('png','*.png'),('jpg','*.jpg'),('ico','*.ico')])
    img.save(name+'.png', 'jpeg')

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title("图片添加数字神器")
    win.geometry('500x300')
    selectbtn = tkinter.Button(win, text='选择图片', width=8, height=2, command=select_pic)
    selectbtn.place(x=20, y=10)

    # tk的Entry不能设置height高度 所以使用Text代替

    num_text = tkinter.Text(win, width=10, height=2)
    num_text.place(x=90,y=10)

    addtbtn = tkinter.Button(win, text='添加内容', width=8, height=2, command=add_num)
    addtbtn.place(x=160, y=10)

    savetbtn = tkinter.Button(win, text='保存图片', width=8, height=2, command=save_pic)
    savetbtn.place(x=230, y=10)

    pic_label= tkinter.Label(win,text='请先选择需要处理的图片', width=80, height=15)
    pic_label.place(x=10, y=55)

    win.mainloop()
