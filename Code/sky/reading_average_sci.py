from PIL import Image
from os import listdir
import os
import os.path
from skimage import io 
import numpy as np 

path = "181221-sky50"
img_names = []
for f in listdir(path):
    if f.endswith(".jpg"):
        img_names.append(path + '/' + f)
img_names = sorted(img_names)

file = open("average_pixel_values.txt", "a")
file.write(path + "\n")

for img_name in img_names:

    # sky = Image.open(img_name)
    # pix = sky.load()
    # sky_grey = Image.open(img_name).convert('L')
    # pix_grey = sky_grey.load()
    sky = io.imread(img_name) 

    # r_total = 0
    # g_total = 0
    # b_total = 0
    # pix_total = sky.size[0] * sky.size[1]

    # bw_total = 0
    # print(img_name)

    # for i in range(sky.size[0]):
    #     for j in range(sky.size[1]):
    #         r_total += pix[i, j][0]
    #         g_total += pix[i, j][1]
    #         b_total += pix[i, j][2]
    #         bw_total += pix_grey[i, j]

    # r_avg = r_total / pix_total
    # g_avg = g_total / pix_total
    # b_avg = b_total / pix_total
    # bw_avg = bw_total / pix_total
    r_avg = np.mean(sky[:,:,0])
    g_avg = np.mean(sky[:,:,1])
    b_avg = np.mean(sky[:,:,2]) 
    bw_avg = (r_avg + g_avg + b_avg) / 3. 
    midival = int(bw_avg*(81.-36.)/255. + 36)
    print(r_avg, g_avg, b_avg, bw_avg, midival)
    file.write("%f, %f, %f, %f, %d\n" % (r_avg, g_avg, b_avg, bw_avg, midival))

print("finished!")
file.close()
