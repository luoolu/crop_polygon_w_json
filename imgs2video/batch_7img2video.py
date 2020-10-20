# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 下午7:29
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_7img2video.py
# @Software: PyCharm


import glob
import json
import os
import cv2

import cv2 as cv

root_path = "/home/luolu/Desktop/particle/沉积岩"
from os.path import isfile, join
out_path = "/home/luolu/Desktop/video_particle/"

if __name__ == '__main__':
    # base_name = ''
    counter = 0
    for filename in sorted(glob.glob(root_path + '/*/*.png')):
        img = cv.imread(filename, 0)
        # height, width, channels = img.shape
        print("file name:\n", filename)
        folder_name = filename.split('/')[-2]
        print("folder_name: ", folder_name)
        counter = counter + 1
        base_name = filename.split('/')[-1]
        # print(filename.split('/')[-1][1:2])
        # if filename.split('/')[-1][1:2].__eq__(1):
        #     print(filename)
        pathIn = root_path + "/" + folder_name + "/"
        pathOut = out_path + "/" + folder_name + ".avi"

        # make video
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





    print("counter: ", counter)