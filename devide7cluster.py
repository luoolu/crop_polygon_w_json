# -*- coding: utf-8 -*-
# @Time    : 2020/10/17 下午7:52
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : test.py
# @Software: PyCharm


import os, os.path, shutil
import errno

folder_path = "/home/luolu/Desktop/test_result/16_胶结物-自生粘土矿物"
out_dir = "/home/luolu/Desktop/particle/胶结物-自生粘土矿物/"

images = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
counter = 0
label = folder_path.split('/')[-1]
print("label:", label)
for image in images:
    file_name = image.split('.')[0].split('_')[-2].split('m')[-2]
    temp1 = image.split('c1')[0]
    temp2 = image.split('c1')[-1]
    if file_name.__eq__('c1'):
        particle_folder_name = temp1 + label + "_" + temp2.split('.')[0]
        # create particle folder
        try:
            os.makedirs(out_dir + particle_folder_name)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        print("temp No:", file_name)
        print("temp No1:", temp1)
        print("temp No2:", temp2)
        print("file_name:", image)
        shutil.copy(folder_path + "/" + temp1 + "c1" + temp2, out_dir + particle_folder_name)
        shutil.copy(folder_path + "/" + temp1 + "c2" + temp2, out_dir + particle_folder_name)
        shutil.copy(folder_path + "/" + temp1 + "c3" + temp2, out_dir + particle_folder_name)
        shutil.copy(folder_path + "/" + temp1 + "c4" + temp2, out_dir + particle_folder_name)
        shutil.copy(folder_path + "/" + temp1 + "c5" + temp2, out_dir + particle_folder_name)
        shutil.copy(folder_path + "/" + temp1 + "c6" + temp2, out_dir + particle_folder_name)
        shutil.copy(folder_path + "/" + temp1 + "c7" + temp2, out_dir + particle_folder_name)
        counter = counter + 1
        print("particle_folder_name: ", particle_folder_name)


print("counter: ", counter)