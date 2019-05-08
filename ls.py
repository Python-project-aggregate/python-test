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
    def _listdir(path, all=False, detail=False, human= False):
        '''详细列出本目录'''
        p = Path(path)
        for f in p.iterdir():
            if not all f.name.startswith('.'):# 不显示隐藏文件
                continue
            if not detail:
                yield (f.name)
            else:
                #
                st = f.stat()
                mode = stat.filemode(st.st_mode)
                mtime = datetime.fromtimestamp(st.st_mtime).strftime('%Y %m %d %H:%M:%S')
                size = st.st_size if not human else _gethuman(st.st_size)
                yield(mode,st.st_nlink, st.st_uid, st.st_gid, size, mtime ,f.name)
    # 排序
    yield from sorted(_listdir(path, all, detail, haman), key = lambda x:x[-1])

if __name__ == '__main__':
    args = parser.parse_args()
    parser.print_help()
    files = listdir(args.path, args.all, args.l, args.human)
    print(list(files))


