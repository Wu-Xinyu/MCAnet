import glob
import os
import glob
import numpy as np
import random
from tqdm import tqdm
from shutil import copy
import pandas as pd
import csv

input_data_path = r'whu-opt-sar\crop'

#将文件名写入列表
test_path = os.path.join(input_data_path, 'test')
test_sar_path = glob.glob(os.path.join(os.path.join(test_path, 'sar'), '*.tif'))
test_opt_path = glob.glob(os.path.join(os.path.join(test_path, 'opt'), '*.tif'))
test_lbl_path = glob.glob(os.path.join(os.path.join(test_path, 'lbl'), '*.tif'))

train_path = os.path.join(input_data_path, 'train')
train_sar_path = glob.glob(os.path.join(os.path.join(train_path, 'sar'), '*.tif'))
train_opt_path = glob.glob(os.path.join(os.path.join(train_path, 'opt'), '*.tif'))
train_lbl_path = glob.glob(os.path.join(os.path.join(train_path, 'lbl'), '*.tif'))

val_path = os.path.join(input_data_path, 'val')
val_sar_path = glob.glob(os.path.join(os.path.join(val_path, 'sar'), '*.tif'))
val_opt_path = glob.glob(os.path.join(os.path.join(val_path, 'opt'), '*.tif'))
val_lbl_path = glob.glob(os.path.join(os.path.join(val_path, 'lbl'), '*.tif'))

# print(val_sar_path[0:10])
# train
print('开始写入数据集')
print("train set")

f = open(os.path.join(input_data_path, 'whu10-train.csv'), 'w', encoding='utf-8', newline="")


csv_write = csv.writer(f)
print(len(train_opt_path))

for i in tqdm(range(0, len(train_sar_path))):

    sar_path = os.path.join(train_sar_path[i]).replace('\\', '/')  #读出的文件是\\ 替换成/
    opt_path = os.path.join(train_opt_path[i]).replace('\\', '/')
    lbl_path = os.path.join(train_lbl_path[i]).replace('\\', '/')

    csv_write.writerow([sar_path, opt_path, lbl_path])


f.close()





# test
print("test set")
f = open(os.path.join(input_data_path, 'whu10-test.csv'), 'w', encoding='utf-8', newline="")

csv_write = csv.writer(f)
for i in tqdm(range(0, len(test_sar_path))):

    sar_path = os.path.join(test_sar_path[i]).replace('\\', '/')
    opt_path = os.path.join(test_opt_path[i]).replace('\\', '/')
    lbl_path = os.path.join(test_lbl_path[i]).replace('\\', '/')

    csv_write.writerow([sar_path, opt_path, lbl_path])
f.close()

print("val set")
f = open(os.path.join(input_data_path, 'whu10-val.csv'), 'w', encoding='utf-8', newline="")

csv_write = csv.writer(f)
for i in tqdm(range(0, len(val_sar_path))):

    sar_path = os.path.join(val_sar_path[i]).replace('\\', '/')
    opt_path = os.path.join(val_opt_path[i]).replace('\\', '/')
    lbl_path = os.path.join(val_lbl_path[i]).replace('\\', '/')

    csv_write.writerow([sar_path, opt_path, lbl_path])
f.close()





