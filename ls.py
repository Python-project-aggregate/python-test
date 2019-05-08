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

