# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 14:38:41
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 15:24:33

#****************************#
#使用带有 open() 函数读写py脚本
#为了写入一个文本文件，使用带有 w 模式的 open() 函数
#****************************#

import os.path
base_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前路径
file_path = os.path.join(base_path, "whiteListNo.py")

with open(file_path, "r", encoding="UTF-8") as f:
    whiteListMonsterNoSet = set()
    lines = f.readlines()
    for line in lines:
        no = line.find('NO_')
        flag = line.find('=')
        if no != -1 and flag != -1 and flag > no:
            monsterno = line[flag+1:].strip()
            whiteListMonsterNoSet.add(int(monsterno))
            # monsterno = line[no+3:flag].strip()
            # whiteListMonsterNoSet.add(int(monsterno))
    print(sorted(list(whiteListMonsterNoSet)))
