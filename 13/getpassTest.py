# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 00:20:34
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 00:22:03

#****************************#
#getpass 很轻松的弹出密码输入提示， 并且不会在用户终端回显密码
#运行时需要一个密码。此脚本是交互式的，因此不能将密码在脚本中硬编码， 而是需要弹出一个密码输入提示，让用户自己输入。
#os.get_terminal_size()  得到当前终端的大小以便正确的格式化输出
#****************************#

import os
import getpass

def svc_login(user,passwd):
    if passwd == 'szj':
    # if user=='szj' and passwd=='szj':
        return True
    else:
        return False

user = getpass.getuser()  #不会弹出用户名的输入提示。 它会根据该用户的shell环境或者会依据本地系统的密码库（支持 pwd 模块的平台）来使用当前用户的登录名
# user = input('Enter your username: ')
passwd = getpass.getpass()

# user = input('Enter your username: ')
# passwd = input('Enter your passwd: ')

if svc_login(user, passwd):    # You must write svc_login()
    print(user,passwd)
    print('Yay!')
else:
    print('Boo!')


sz = os.get_terminal_size()
print(sz,sz.lines,sz.columns)