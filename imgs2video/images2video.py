# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 上午9:08
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : images2video.py
# @Software: PyCharm

import cv2
import numpy as np
import os
from os.path import isfile, join

pathIn = '/home/luolu/PycharmProjects/crop_polygon_w_json/image/4/'
pathOut = '/home/luolu/PycharmProjects/crop_polygon_w_json/video/video_4.avi'
fps = 1
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x)
files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x)
for i in range(len(files)):
    filename = pathIn + files[i]
    # reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
