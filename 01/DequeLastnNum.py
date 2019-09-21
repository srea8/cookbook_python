# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-08 13:04:03
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:06:59


#****************************#
#####队列的用法#####
#****************************

from collections import deque

q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.appendleft(12)
d=q.popleft()
print (q)
print (d)