# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 17:17:43
# @Last Modified by:   srea
# @Last Modified time: 2019-09-24 21:33:18

#****************************#
#想从左至右将其解析为一个令牌流
#####构建pat的时候需要注意 
# 正则表达式指定了所有输入中可能出现的文本序列：第一点就是你必须确认你使用正则表达式指定了所有输入中可能出现的文本序列。 如果有任何不可匹配的文本出现了，扫描就会直接停止
# 长模式写在前面：令牌的顺序也是有影响的。 re 模块会按照指定好的顺序去做匹配。 因此，如果一个模式恰好是另一个更长模式的子字符串，那么你需要确定长模式写在前面
#****************************#

text = "foo = 23 + 42 * 10"

import re

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))
print(master_pat)



scanner = master_pat.scanner(text)
print(scanner.match())   #按照顺序进行匹配，匹配完成后输出
print(scanner.match())

for m in iter(scanner.match,None):    #按照顺序进行匹配，匹配完成后输出
	print(m)
	print(m.lastgroup,m.group())


# 将上面内容写成函数
from collections import namedtuple

def generate_tokens(pat,text):
	Token = namedtuple('Token',['type','value'])
	scanner = pat.scanner(text)
	for m in iter(scanner.match,None):
		yield Token(m.lastgroup,m.group())

for tok in generate_tokens(master_pat,text):
	print ('{:>10s} {:>10s}'.format(tok.type,tok.value))

print('\n')

tokens = (tok for tok in generate_tokens(master_pat,text) if tok.type != 'WS') #过滤字符WS
for tok in tokens:
	print ('{:>10s} {:>10s}'.format(tok.type,tok.value))



#####注意构建的token顺序
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

ss_pat = re.compile('|'.join([LT,LE,EQ]))    #这种构建方式结果为LT <   EQ =
# ss_pat = re.compile('|'.join([LE,LT,EQ]))    #这种构建方式结果为LE <=  
print(ss_pat)

text1 = '<='

ss_scanner = ss_pat.scanner(text1)
for ss in iter(ss_scanner.match,None):
	print(ss.lastgroup,ss.group())

