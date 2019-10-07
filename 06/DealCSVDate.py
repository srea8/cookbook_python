# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-06 22:46:27
# @Last Modified by:   srea
# @Last Modified time: 2019-10-07 18:26:25

#****************************#
#读写一个CSV格式的文件
#大多数的CSV格式的数据读写问题，都可以使用 csv 库
#****************************#

import csv
from collections import namedtuple


##############读csv数据###############

# 将这些数据读取为一个元组的序列
with open('stocks.csv') as f:
	f_csv = csv.reader(f)
	headers = next(f_csv)
	# print(headers)
	Row = namedtuple('Row',headers)   #这种下标访问通常会引起混淆，你可以考虑使用命名元组
	for r in f_csv:
		row = Row(*r)
		print(headers[0],row.Symbol,sep = '   ')   #它允许你使用列名如 row.Symbol 和 row.Change 代替下标访问

with open('stocks.csv') as f:
    f_tsv = csv.reader(f, delimiter='\t')     ####想读取以tab分割的数据，可以这样做
    for row in f_tsv:
    	print(row)



# 将数据读取到一个字典序列中去
with open('stocks.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		print (row['Price'])   #你可以使用列名去访问每一行的数据了



##############写csv数据###############
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
         ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
         ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
       ]

with open('stocks.csv','w',newline = '') as f:    ##'w' 写入   'a' 追加
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)



headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open('stocks.csv','a', newline='') as f:     #一定要加这个newline，不然会有空行
    f_csv = csv.DictWriter(f, headers)
    # f_csv.writeheader()
    f_csv.writerows(rows)