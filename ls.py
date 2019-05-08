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
def _getfiletype(f:Path):
    if f.is_dir():
        return 'd'
    elif f.is_char_device():
        return 'c'
    elif f.is_socket():
        return 's'
    elif f.is_symlink():
        return 'l'
    else:
        return '-'
# -rw-rw-r-- 1 python python
def listdirdetail(path, all=False):
    '''详细列出本目录'''
    p = Path(path)
    for f in p.iterdir():
        if not all and f.name.startswith('.'):
            continue
            # mode 硬链接 属组 属组 字节 时间 name
        stat = f.stat()
        t = _getfiletype(f)
        mode = oct(stat.st_atime)[-3:]