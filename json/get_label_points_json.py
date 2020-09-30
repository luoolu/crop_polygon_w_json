# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 上午9:42
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : get_label_points_json.py
# @Software: PyCharm


import json
import sys
import numpy as np

# load the data into an element
json_file = "/home/luolu/Downloads/data/zhutibaopian/m04/c1m04.json"



with open(json_file) as f:
    data = json.load(f)

# print the resp
# print(data)


# extract an element in the response
for k in data:
    if k == 'shapes':
        # print(k)
        # print(data[k])
        for item in range(len(data[k])):
            # print(item)
            print(data[k][item]['label'])
            sub_img_name = data[k][item]['label']
            print(type(data[k][item]['points']))
            points_list = data[k][item]['points']
            points = np.asarray(points_list)
            print(data[k][item]['points'])

# print(data)