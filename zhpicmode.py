#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Nil'
from PIL import Image
import zhstr
import yinyini
import PicInfo
import os

def zhpicmode(pic,mode):
    avatar = Image.open(pic)
    f,e = os.path.splitext(pic)
    mode1 = unicode(mode)
    newname = f + u'.' +mode1
    newname1 = str(newname)
    pic_change = avatar.save(newname1,mode)
    return pic_change

if __name__ =='__main__':
    ini_file = 'Pic.ini'
    pic_config = zhstr.zhstr()
    pic = yinyini.yinyini(pic_config, ini_file)
    getpic = PicInfo.getpicinfo(pic.pic_addr)
    picchange = zhpicmode(pic.pic_addr,'png')
    print getpic
