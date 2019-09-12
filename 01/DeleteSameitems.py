#_*_ coding:utf-8 _*_
#怎样在一个序列上面保持元素顺序的同时消除重复的值？


# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题
def deque(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,3,1,2,4,5,1,2,4,5]
print(set(a))            ####这种方法不能维护元素的顺序，生成的结果中的元素位置被打乱
print(a)
print(list(deque(a)))


# 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下
def dedque(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

b = [{'1':1,'2':2},{'1':1,'2':2},{'1':2,'2':3},{'1':2,'2':2},]
print(list(dedque(b, key=lambda k:(k['1'],k['2']))))
print(list(dedque(a)))


# 如果如果你想读取一个文件，消除重复行，你可以很容易像这样做
# with open(somefile,'r') as f:
# for line in dedupe(f):
#     print(line)