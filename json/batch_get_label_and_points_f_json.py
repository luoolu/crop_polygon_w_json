# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 上午9:58
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_get_label_and_points_f_json.py
# @Software: PyCharm
import errno
import glob
import json
import os

import cv2 as cv
import numpy as np

content_path = "/home/luolu/Desktop/test/1-ning71x-16-0672_m001/"


if __name__ == '__main__':
    base_name = ''
    counter = 0
    sub_counter = 0
    for filename in sorted(glob.glob('/home/luolu/Desktop/test/*/*.json')):
        # img = cv.imread(filename, 0)
        # height, width, channels = img.shape
        print("file name:\n", filename)
        folder_name = filename.split("/")[-2]
        base_name = os.path.basename(filename)
        print("folder name:\n", folder_name)
        imagePath = filename.split(".")[0] + ".png"
        print("imagePath:\n", imagePath)
        img = cv.imread(imagePath)
        with open(filename) as f:
            data = json.load(f)

        # extract an element in the response
        for k in data:
            if k == 'shapes':
                # print(k)
                # print(data[k])
                for item in range(len(data[k])):

                    # print(item)
                    print("label:", data[k][item]['label'])
                    sub_img_name = data[k][item]['label']
                    # make folder for label
                    # if os.path.exists("/home/luolu/PycharmProjects/crop_polygon_w_json/image/" + sub_img_name):
                    #     sub_counter = sub_counter + 1
                    #     try:
                    #         os.makedirs(
                    #             "/home/luolu/PycharmProjects/crop_polygon_w_json/image/" + sub_img_name + "_" + str(
                    #                 sub_counter))
                    #     except OSError as e:
                    #         if e.errno != errno.EEXIST:
                    #             raise
                    # else:
                    try:
                        os.makedirs("/home/luolu/Desktop/test_result/" + sub_img_name)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise
                    # print(type(data[k][item]['points']))
                    points_list = data[k][item]['points']
                    # print("points_list:\n", data[k][item]['points'])
                    points = np.asarray(points_list)
                    points[points < 0] = 0
                    # print("points:\n", points)
                    points = np.around(points)
                    points = points.astype(int)

                    print("int points:\n", points)

                    # # (1) Crop the bounding rect
                    rect = cv.boundingRect(points)
                    x, y, w, h = rect
                    croped = img[y:y + h, x:x + w].copy()

                    # # (2) make mask
                    points = points - points.min(axis=0)

                    mask = np.zeros(croped.shape[:2], np.uint8)
                    cv.drawContours(mask, [points], -1, (255, 255, 255), -1, cv.LINE_AA)

                    # # (3) do bit-op
                    dst = cv.bitwise_and(croped, croped, mask=mask)

                    # # (4) add the white background
                    bg = np.ones_like(croped, np.uint8) * 255
                    cv.bitwise_not(bg, bg, mask=mask)
                    dst2 = bg + dst

                    counter = counter + 1
                    # cv.imwrite("/home/luolu/PycharmProjects/crop_polygon_w_json/image/croped_" + base_name + sub_img_name + ".png", croped)
                    # cv.imwrite("/home/luolu/PycharmProjects/crop_polygon_w_json/image/mask_" + base_name + sub_img_name + ".png", mask)
                    # print("/home/luolu/PycharmProjects/crop_polygon_w_json/image/"
                    #       + sub_img_name + "/" + imagePath.split('.')[0] + "_" + str(item) + ".png")

                    if item < 10:
                        cv.imwrite("/home/luolu/Desktop/test_result/"
                               + sub_img_name + "/" + folder_name + "_" + imagePath.split('/')[-1].split('.')[-2] + "_0" + str(item) + ".png", dst)
                    else:
                        cv.imwrite("/home/luolu/Desktop/test_result/"
                                   + sub_img_name + "/" + folder_name + "_" + imagePath.split('/')[-1].split('.')[-2] + "_" + str(item) + ".png", dst)

    print("counter:", counter)
