'''
logstash 收集日志 elasticsearch
kibanna则从es集群中查询数据生成图表返回浏览器端
从test提取数据
使用正则提取分组
日志产出采集 存储 分析 存储 可视化
类型转换:时间转换 datatime.strptime
状态码和字节数用int函数转换
映射:对每一个字段命名
异常处理日志会出现一些不匹配的行,需要处理
re.match方法,采用抛出异常的方式,让调用者获得异常并自行处理.
数据载入:日志,载入数据就是文件io的读取, 将获取数据的方法封装成函数.load
日志文件的加载,迭代一下路径文件的存放,判断路径是一个目录还是文件.
分析器:分析IP的地理分布, 用对列,pv分析,user-agent模块. 可以用第三方模块.
'''
with open('test.log') as f:
    for line in f:
        for field in line.split():
            print(field)

import re
pattern = '''
([\d.]{7,})
'''
regex =  re.compile(pattern)
def extract(logline:str):
    m = regex.match(logline)
    if m:
        print(m.group())
extract(line)

import datetime
def convert_time(timestr):
    return datetime.datetime.striptime(timestr, '%d/%b/%Y: %H:%M:%s')
lambda timestr: datetime.datetime.strip(timestr, '%d')