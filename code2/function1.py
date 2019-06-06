'''
python 常用模块
-运行时服务相关模块 copy pickle sys
-数学相关模块 decimal math randon
-字符串相关模块 codecs re
文件处理相关模块 datetime os time logging io
进程和线程相关模块 ftplib http smtplib urllib
web编程相关模块 cgi webbrowser
数据处理和编码模块 base64 csv html.parser json xml

'''
import time
import shutil
import os
seconds =  time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%h:%S', localtime)
print(strtime)

