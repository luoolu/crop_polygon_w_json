#  pngs to mp4

ffmpeg -r 1/7 -i c%dm04_1.png -c:v libx264 -vf fps=1 -pix_fmt yuv420p -vf pad="width=ceil(iw/2)*2:height=ceil(ih/2)*2" out.mp4


#  crop image from labelme polygon json

python batch_get_label_and_points_f_json.py