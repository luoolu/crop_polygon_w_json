# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 上午9:32
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : copy_json_for075.py
# @Software: PyCharm


import os
from shutil import copyfile
counter = 5
exist_couter = 0

for i in range(0, 100, 1):
    print(i)
    if i < 10 and os.path.exists("/home/luolu/Desktop/test/1-ning71x-16-0672_m00" + str(i)):
        exist_couter = exist_couter + 1
        directory = "/home/luolu/Desktop/test/1-ning71x-16-0672_m00" + str(i)
        json_file_path = ""

        for filename in os.listdir(directory):
            # print(filename)
            if filename.endswith('.json'):
                # print(filename)
                json_file_path = directory + "/" + filename
                # print(json_file_path)

        # print(json_file_path)
        # copyfile(src, dst)
        for filename in os.listdir(directory):
            # print(filename.split(".")[-1])
            # print(json_file_path.split("/")[-1].split(".")[0])
            if os.path.isfile(
                    directory + "/" + json_file_path.split("/")[-1].split(".")[0] + ".png") and filename.endswith(
                    '.json'):
                print("json file: ", filename)
            elif filename.split('.')[0] != json_file_path.split("/")[-1].split(".")[0]:
                print(filename)
                # src = json file
                # dst = directory + "/" + filename
                # print(directory + "/" + filename.split(".")[0] + ".json")
                copyfile(src=json_file_path, dst=directory + "/" + filename.split(".")[0] + ".json")
    if i >= 10 and os.path.exists("/home/luolu/Desktop/test/1-ning71x-16-0672_m0" + str(i)):
        exist_couter = exist_couter + 1
        directory = "/home/luolu/Desktop/test/1-ning71x-16-0672_m0" + str(i)
        json_file_path = ""

        for filename in os.listdir(directory):
            # print(filename)
            if filename.endswith('.json'):
                # print(filename)
                json_file_path = directory + "/" + filename
                # print(json_file_path)

        # print(json_file_path)
        # copyfile(src, dst)
        for filename in os.listdir(directory):
            # print(filename.split(".")[-1])
            # print(json_file_path.split("/")[-1].split(".")[0])
            if os.path.isfile(
                    directory + "/" + json_file_path.split("/")[-1].split(".")[0] + ".png") and filename.endswith(
                    '.json'):
                print("json file: ", filename)
            elif filename.split('.')[0] != json_file_path.split("/")[-1].split(".")[0]:
                print(filename)
                # src = json file
                # dst = directory + "/" + filename
                # print(directory + "/" + filename.split(".")[0] + ".json")
                copyfile(src=json_file_path, dst=directory + "/" + filename.split(".")[0] + ".json")
print("exist_couter: ", exist_couter)
