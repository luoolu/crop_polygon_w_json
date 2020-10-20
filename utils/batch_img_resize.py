# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 下午9:23
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_img_resize.py
# @Software: PyCharm


from PIL import Image
import os, sys
import glob
counter = 0
path = "/home/luolu/Desktop/particle/*/*/*.png"
# dirs = os.listdir(glob.glob("/home/luolu/Desktop/particle/01_石英/*/*.png"))
for file in glob.glob("/home/luolu/Desktop/particle_img256/*/*/*.png"):
    print(file)
    im = Image.open(file)
    counter = counter + 1
    imResize = im.resize((256, 256), Image.ANTIALIAS)
    imResize.save(file, 'PNG', quality=100)


print("counter: ", counter)
# def resize():
#     for item in dirs:
#         if os.path.isfile(path + item):
#             im = Image.open(path + item)
#             f, e = os.path.splitext(path + item)
#             print(f)
#             imResize = im.resize((256, 256), Image.ANTIALIAS)
            # imResize.save(f + ' resized.jpg', 'JPEG', quality=90)


# resize()
