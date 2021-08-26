#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt

if __name__ == "__main__":
    argv = sys.argv[1:]
    tips = '''
                        python run.py -h 查看帮助
                        python run.py -t
                        参数选项：
                        1： 一般树
                        2： 搜索二叉树
                        3： 平衡二叉树
                '''
    if len(argv) == 0:
        print(tips)
        exit(0)

    try:
        opts, args = getopt.getopt(argv, "t:h")
    except Exception as e:
        print(tips)
        exit(-1)

    for opt, arg in opts:
        if opt == '-h':
            print(tips)
