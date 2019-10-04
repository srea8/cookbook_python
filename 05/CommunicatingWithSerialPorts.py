# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-03 11:22:36
# @Last Modified by:   srea
# @Last Modified time: 2019-10-03 11:34:48

#****************************#
#通过串行端口读写数据，典型场景就是和一些硬件设备打交道
#串行通信最好的选择是使用 pySerial包
#在Windows系统上，你可以使用0, 1等表示的一个设备来打开通信端口”COM0”和”COM1”
#****************************#


# 所发十六进制字符串010591F50000F104
cmd = [0x01, 0x05, 0x91, 0xF5, 0x00, 0x00, 0xF1, 0x04]

import serial
import serial.tools.list_ports


class ser(object):
	"""docstring for ser"""
	def __init__(self,portname):
		self.port = serial.Serial(port = portname,baudrate = 9600,bytessize = 8,parity = 'E',stopbits = 1,timeout = 60)

	def send_cmd(self,cmd):
		self.port.write(cmd)
		response = self.port.readall()
		response = self.convert_hex(response)
		return response

	def convert_hex(self,string):
		res = []
		result = []
		for item in string:
			res.append(item)
		for i in res:
			result.append(hex(i))
		return result



def FindPort():
	plist = list(serial.tools.list_ports.comports())

	if len(plist) <= 0:
		print('Not Find Port!!')
	else:
		plist_0 = list(plist[0])
		serialName = plist_0[0]
		serialFd = serial.Serial(serialName,9600,timeout = 60)
		print("Port>>>",serialFd.name)

FindPort()