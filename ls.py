#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
from datetime import datetime
# 获得一个参数解析器
parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
parser.add_argument('path', nargs='?',default='.',help='directory')
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore')


args = parser.parse_args() # 分析参数, 同时传入可迭代的参数
# parser.print_help()
print(args) # 打印名词空间中收集的参数
parser.print_help()

def listdir(path, all=False):
    '''列出本目录文件'''
    p = Path(path)
    # for f in p.iterdir():
    #       if not all and f.name.startswith('.') # 不显示隐藏文件
    #           continue
    #        yield f.name
    # yield from filter(lambda f:not (not all and f.name,startswith('.')), p.iterdir())
    # yield from filter(lambda f:all or not f.name.startswith('.'), p.iterdir())
    yield from filter(lambda f:all or not f.name.startswith('.'), p.iterdir())

# 获取文件类型


