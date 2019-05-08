#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from pathlib import Path
from datetime import datetime
import stat
# 获得一个参数解析器
parser = argparse.ArgumentParser(prog = 'ls', add_help=False, description='list directory')
parser