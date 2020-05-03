# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 15:37:00
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 15:37:23

#****************************#
#在脚本和程序中将诊断信息写入日志文件
#打印日志最简单方式是使用 logging 模块
# 五个日志调用（critical(), error(), warning(), info(), debug()）以降序方式表示不同的严重级别
#****************************#

import time
import logging
import logging.config





def gettime():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def main():
    logging.basicConfig(
        # filename='app.log',        #屏蔽后默认在控制台输出
        level=logging.ERROR,         # 参数 level 是一个过滤器。 所有级别低于此级别的日志消息都会被忽略掉
        format='%(levelname)s:%(asctime)s:%(message)s'          #自定义输出格式
    )
    print(logging.getLogger(__name__))
    logging.getLogger().level = logging.DEBUG  #basicConfig() 在程序中只能被执行一次。如果你稍后想改变日志配置， 就需要先获取 root logger ，然后直接修改它

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

    #自定义时间
    # logging.critical('[%s] -- Host %s unknown', gettime(),hostname)
    # logging.error("[%s] -- Couldn't find %r", gettime(),item)
    # logging.warning('[%s] -- Feature is deprecated', gettime())
    # logging.info('[%s] -- Opening file %r, mode=%r', gettime(),filename, mode)
    # logging.debug('[%s] -- Got here', gettime())


    logging.config.fileConfig('logconfig.ini')
    logging.info('[%s] -- Opening file %r, mode=%r', gettime(),filename, mode)
    logging.debug('[%s] -- Got here', gettime())


if __name__ == '__main__':
    main()
