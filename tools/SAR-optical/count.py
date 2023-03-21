import os, glob
from PIL import  Image
import numpy as np

from collections import Counter


#统计前11张图片中每个类别怎么表示的以及出现的次数

root = r'whu-opt-sar\\newlbl'
files = os.listdir(root) # 1-7
# print(files[0:11])


#   取出lbl文件中的11个（tif文件是一种图片格式，可以用PIL库打开）
for file in files[0:11]:
    data = np.array(Image.open(os.path.join(root, file))) #将读取到的图片转换为数组（3704*5556）
    # print(data)
    unique, count = np.unique(data, return_counts=True)   #统计数组中每个值出现的次数
    # print(unique, count)
    data_count = dict(zip(unique, count))
    print(data_count)    #打印出每个值(类别）出现的次数

# if __name__ == '__main__':
#     x = [1,2,3,4,5][2:4]
#     print(x)