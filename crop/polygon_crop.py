# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 上午8:51
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : polygon_crop.py
# @Software: PyCharm

import numpy as np
import cv2

img = cv2.imread("/home/luolu/Downloads/data/zhutibaopian/m04/c1m04.png")
pts = np.array([[10, 150], [150, 100], [300, 150], [350, 100], [310, 20], [35, 10]])

#   # (1) Crop the bounding rect
rect = cv2.boundingRect(pts)
x, y, w, h = rect
croped = img[y:y + h, x:x + w].copy()

#   # (2) make mask
pts = pts - pts.min(axis=0)

mask = np.zeros(croped.shape[:2], np.uint8)
cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

#   # (3) do bit-op
dst = cv2.bitwise_and(croped, croped, mask=mask)

#   # (4) add the white background
bg = np.ones_like(croped, np.uint8) * 255
cv2.bitwise_not(bg, bg, mask=mask)
dst2 = bg + dst

cv2.imwrite("image/croped.png", croped)
cv2.imwrite("image/mask.png", mask)
cv2.imwrite("image/dst.png", dst)
cv2.imwrite("image/dst2.png", dst2)
