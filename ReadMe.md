#  pngs to mp4

ffmpeg -r 1/7 -i c%dm04_1.png -c:v libx264 -vf fps=1 -pix_fmt yuv420p -vf pad="width=ceil(iw/2)*2:height=ceil(ih/2)*2" out.mp4


#  crop image from labelme polygon json

python batch_get_label_and_points_f_json.py

#   zhutibaopian crop
##  1,copy json for zhengjiao image     copy_json_for075.py
##  2,modify json                       batch_mdf_json.py
##  3,crop from json                    batch_get_label_and_points_f_json.py
##  4,div particle                      devide7cluster.py
##  5,images to video                   images2video.py

