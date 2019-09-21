# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 14:12:12
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:08:17


#****************************#
## 怎样找出一个序列中出现次数最多的元素呢？
#****************************#

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under',
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under',
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)

print(word_counts)
word_counts.update(words)     #增加
print(word_counts)
word_counts.subtract(words)      #减少
print(word_counts)
print(word_counts.get('look'))
print(word_counts.popitem())
print(top_three)