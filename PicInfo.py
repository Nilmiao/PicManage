#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__='Nil'
from PIL import Image
import zhstr
import yinyini

def getpicinfo(pic):
    avatar = Image.open(pic)
    pic_format = avatar.format
    pic_size = avatar.size
    pic_mode = avatar.mode
    return  pic_format,pic_size,pic_mode

if __name__ =='__main__':
    ini_file = 'Pic.ini'
    pic_config = zhstr.zhstr()
    pic = yinyini.yinyini(pic_config, ini_file)
    getpic = getpicinfo(pic.pic_addr)
    print getpic
