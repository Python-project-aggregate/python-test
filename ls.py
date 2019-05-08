#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
from datetime import datetime
import stat
# 获得一个参数解析器
parser = argparse.ArgumentParser(prog = 'ls', add_help=False, description='list directory')
parser.add_argument('path', nargs='?', default='.', help = "directory")
parser.add_argument('-l', action='store_true', help='use a long listing format')
parser.add_argument('-a', '--all', action='store_true', help= 'show all files')
parser.add_argument('-h', '--human-readable', action='store_true')
def listdir(path, all= False, detail=False,human=False):
    def _gethuman(size:int):
        units = 'KMGTP'
        depth = 0
        while size > 1000 and depth + 1< len(units):
            # 当天size大于1000, 且depth不是最后一个
            size = size // 1000
            depth += 1
        return "{}{}".format(size, units[depth])
    def _list