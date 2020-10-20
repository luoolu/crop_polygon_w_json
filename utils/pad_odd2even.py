# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 下午6:32
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : pad_odd2even.py
# @Software: PyCharm


import cv2
import numpy as np
import math
from PIL import Image
# read image, ensure binary
img = cv2.imread('/home/luolu/PycharmProjects/crop_polygon_w_json/image/1/c1m04_1.png')
height, width, channels = img.shape
print(height)
print(width)


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

print(new_width, new_height)
top, bottom = new_height, 0
left, right = new_width, 0

color = [0, 0, 0]
newsize = (new_width, new_height)
# save result
# resize image
output = cv2.resize(img, newsize)

cv2.imwrite('/home/luolu/PycharmProjects/crop_polygon_w_json/image/1/new_im_c1m04_1.png', output)

