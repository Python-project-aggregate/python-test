#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
# 获得一个参数解析器
parser = argparse.ArgumentParser(prog='ls', add_help=True, description='list directory contents')
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true', help='show all files, do not ignore')


args = parser.parse_args() # 分析参数, 同时传入可迭代的参数
# parser.print_help()
print(args) # 打印名词空间中收集的参数
parser.print_help()
# 运行结果


