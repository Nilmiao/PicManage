#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Nil'
import configparser
def duquini(zhstr,init_file):
    config = configparser.ConfigParser()
    config.read(init_file)
    zhstr.pic_addr = config['DEFAULT']['pic_addr']
    return zhstr
