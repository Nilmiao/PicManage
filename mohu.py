#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__='Nil'
from PIL import Image,ImageFilter
import zhstr
import yinyini
import os
import PicInfo

def mohu(pic):
    avatar = Image.open(pic)
    f,e = os.path.splitext(pic)
    avatar1 = avatar.filter(ImageFilter.FIND_EDGES)
    newname = f + u'mohu' + e
    newname1 = str(newname)
    pic_change = avatar1.save(newname1)
    return pic_change

if __name__ =='__main__':
    ini_file = 'Pic.ini'
    pic_config = zhstr.zhstr()
    pic = yinyini.yinyini(pic_config, ini_file)
    getpic = PicInfo.getpicinfo(pic.pic_addr)
    picchange = mohu(pic.pic_addr)
    print getpic