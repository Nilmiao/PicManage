#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__='Nil'
from PIL import Image
import zhstr
import yinyini
import os
import PicInfo

def suolvtu(pic):
    avatar = Image.open(pic)
    f,e = os.path.splitext(pic)
    newname = f + u'duibian' + e
    newname1 = str(newname)
    w,h=avatar.size
    avatar.thumbnail((w//2,h//2))
    pic_change = avatar.save(newname1)
    return pic_change

if __name__ =='__main__':
    ini_file = 'Pic.ini'
    pic_config = zhstr.zhstr()
    pic = yinyini.yinyini(pic_config, ini_file)
    getpic = PicInfo.getpicinfo(pic.pic_addr)
    picchange = suolvtu(pic.pic_addr)
    print getpic