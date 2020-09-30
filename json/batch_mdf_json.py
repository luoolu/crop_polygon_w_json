# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 上午9:25
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_mdf_json.py
# @Software: PyCharm


import glob
import json
import os

import cv2 as cv

from json.get_keyV_json import updateJsonFile

if __name__ == '__main__':
    base_name = ''
    counter = 0
    for filename in sorted(glob.glob('/home/luolu/Downloads/data/zhutibaopian/m04/*.json')):
        img = cv.imread(filename, 0)
        # height, width, channels = img.shape
        print("file name:\n", filename)
        folder_name = os.path.basename(filename)
        print("folder name:\n", folder_name.split(".")[0])
        imagePath = folder_name.split(".")[0] + ".png"
        print("imagePath:\n", imagePath)
        # base_name = os.path.basename(filename)
        with open(filename) as f:
            data = json.load(f)

        # print the resp
        # print(data)

        # extract an element in the response
        for k in data:
            if k == 'imagePath':
                # print(k)
                print(data[k])
                updateJsonFile(file=filename, value=imagePath)

        print(data)
