# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 下午7:51
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_pad_odd2even.py
# @Software: PyCharm


import glob
import math
import os

import cv2
import numpy as np

if __name__ == '__main__':
    base_name = ''
    counter = 0
    for filename in sorted(glob.glob('/home/luolu/Desktop/test_result/*/*.png')):
        img = cv2.imread(filename)
        # height, width, channels = img.shape
        print(filename)
        base_name = os.path.basename(filename)
        folder_name = filename.split('/')[-2]
        print("folder_name: ", folder_name)
        height, width, channels = img.shape
        print(str(width) + " X " + str(height))

        # new image H, W
        new_height = 0
        new_width = 0

        # pad=ceil(iw/2)*2:ceil(ih/2)*2

        if (height % 2) == 0:
            new_height = height
        else:
            new_height = math.ceil(height / 2) * 2
        if (width % 2) == 0:
            new_width = width
        else:
            new_width = math.ceil(width / 2) * 2

        print(str(new_width) + " X " + str(new_height))
        top, bottom = new_height, 0
        left, right = new_width, 0

        color = [0, 0, 0]
        newsize = (new_width, new_height)
        # save result
        # resize image
        output = cv2.resize(img, newsize)

        cv2.imwrite("/home/luolu/Desktop/test_result/" + folder_name + "/" + base_name, output)
        counter = counter + 1
    print("counter: ", counter)