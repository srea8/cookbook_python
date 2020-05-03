# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-04-25 23:01:28
# @Last Modified by:   srea
# @Last Modified time: 2020-04-25 23:33:18

#****************************#
# 对象池模式, 或者称为对象池服务, 其意图为: 通过循环使用对象, 减少资源在初始化和释放时的昂贵损耗
# 在实际应用中还需要考虑池的最小值、最大值、池化对象状态(若有,重点考虑)、异常处理(如满池情况)等方面,特别是池化对象状态
# 注意：基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
#****************************#

class QueueObject():
    def __init__(self,queue,auto_get=False):
        self._queue = queue
        self.object = self._queue.get() if auto_get else None

    def __enter__(self):
        print('从对象池中获取对象')
        if self.object is None:
            self.object = self._queue.get()
        return self.object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.object is not None:
            print('将使用完成的对象返回对象池中')
            self._queue.put(self.object)
            self.object = None

    def __del__(self):
        print('调用销毁对象')
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None

def main():
    try:
        import queue
    except ImportError:
        import Queue as queue

    def test_object(queue):
        queue_object = QueueObject(queue,True)
        print('内部 func:{}'.format(queue_object.object))

    sample_queue = queue.Queue()
    sample_queue.put('yam')

    with QueueObject(sample_queue) as obj:
        print('inside with:{}'.format(obj))
    # print('outside with:{}'.format(sample_queue.get()))

    sample_queue.put('sam')
    test_object(sample_queue)

    print('外部func：{}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())

if __name__ == '__main__':
    main()
