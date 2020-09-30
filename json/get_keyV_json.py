# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 上午9:25
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : get_keyV_json.py
# @Software: PyCharm


import json
import sys

# load the data into an element
json_file = "/home/luolu/Downloads/data/zhutibaopian/m04/c1m04.json"


def updateJsonFile(file, value):
    jsonFile = open(file, "r")  # Open the JSON file for reading
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file

    ## Working with buffered content
    tmp = data["imagePath"]
    data["imagePath"] = value
    data["imageData"] = None

    ## Save our changes to JSON file
    jsonFile = open(file, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()


with open(json_file) as f:
    data = json.load(f)

# print the resp
# print(data)


# extract an element in the response
for k in data:
    if k == 'shapes':
        # print(k)
        print(data[k])
        # updateJsonFile(file=json_file, value="kkk")

print(data)