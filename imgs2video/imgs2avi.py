# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 下午3:09
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : imgs2avi.py
# @Software: PyCharm


import cv2
import os

image_folder = '/home/luolu/PycharmProjects/crop_polygon_w_json/image/1'
video_name = '/home/luolu/PycharmProjects/crop_polygon_w_json/video/video_1.avi'

images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(filename=video_name, fourcc=0, fps=1, frameSize=(width, height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
