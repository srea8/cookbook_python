####队列的用法#####

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