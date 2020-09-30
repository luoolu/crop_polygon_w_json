# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 上午9:24
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_rename.py
# @Software: PyCharm


import glob
import os

import cv2 as cv
import numpy as np


# path = "D:\\data\\pore_throat\\16-0508"
# folder_name = os.path.basename(path)
# print(folder_name)

if __name__ == '__main__':
    base_name = ''
    counter = 0
    for folder_name in sorted(glob.glob('D:\\data\\pore_throat\\*')):
        print(folder_name)
        # base_name = os.path.basename(filename)
        for filename in os.listdir(folder_name):
            # print(filename)
            print(folder_name + "\\" + folder_name.split(".")[2] + "_" + filename)
            # os.rename(src=path + "\\" + filename, dst=path + "\\" + folder_name + "_" + filename)
