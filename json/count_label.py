# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 上午11:56
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : count_label.py
# @Software: PyCharm


import collections
import json
import os
import os.path as osp
import pprint


annotated_dir = '/home/luolu/Downloads/data/zhutibaopian/ZSY_薄片标注_修改_39_1019/yunce_39_1019'
counter = collections.Counter()
for dirpath, dirnames, filenames in os.walk(annotated_dir):
    for filename in filenames:
        if osp.splitext(filename)[-1] != '.json':
            continue
        filename = osp.join(dirpath, filename)
        print(filename)

        with open(filename) as f:
            data = json.load(f)
        for shape in data['shapes']:
            counter[shape['label']] += 1

print('---')

print('# of Labels')
for label, count in counter.items():
    print('{:>10}: {}'.format(label, count))