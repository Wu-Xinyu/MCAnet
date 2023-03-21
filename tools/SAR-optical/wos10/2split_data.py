import glob
import os
import glob
import numpy as np
import random
from tqdm import tqdm
from shutil import copy

###分割数据集，将数据集分为训练集、验证集、测试集6:2:2
input_data_path = r'whu-opt-sar\\crop'

# 获取所有图像的路径
input_sar_path = glob.glob(os.path.join(os.path.join(input_data_path, 'sar'), '*.tif'))
input_opt_path = glob.glob(os.path.join(os.path.join(input_data_path, 'optical'), '*.tif'))
input_lbl_path = glob.glob(os.path.join(os.path.join(input_data_path, 'newlbl'), '*.tif'))

print(input_sar_path, input_opt_path, input_lbl_path)
print('共有{}对影像'.format(len(input_opt_path)))

#新建一些文件夹
test_path = os.path.join(input_data_path, 'test')
if not os.path.exists(test_path):
    os.makedirs(test_path)
test_sar_path = os.path.join(test_path, 'sar')
test_opt_path = os.path.join(test_path, 'opt')
test_lbl_path = os.path.join(test_path, 'lbl')
if not os.path.exists(test_sar_path):
    os.makedirs(test_sar_path)
if not os.path.exists(test_opt_path):
    os.makedirs(test_opt_path)
if not os.path.exists(test_lbl_path):
    os.makedirs(test_lbl_path)

train_path = os.path.join(input_data_path, 'train')
if not os.path.exists(train_path):
    os.makedirs(train_path)
train_sar_path = os.path.join(train_path, 'sar')
train_opt_path = os.path.join(train_path, 'opt')
train_lbl_path = os.path.join(train_path, 'lbl')
if not os.path.exists(train_sar_path):
    os.makedirs(train_sar_path)
if not os.path.exists(train_opt_path):
    os.makedirs(train_opt_path)
if not os.path.exists(train_lbl_path):
    os.makedirs(train_lbl_path)

val_path = os.path.join(input_data_path, 'val')
if not os.path.exists(val_path):
    os.makedirs(val_path)
val_sar_path = os.path.join(val_path, 'sar')
val_opt_path = os.path.join(val_path, 'opt')
val_lbl_path = os.path.join(val_path, 'lbl')
if not os.path.exists(val_sar_path):
    os.makedirs(val_sar_path)
if not os.path.exists(val_opt_path):
    os.makedirs(val_opt_path)
if not os.path.exists(val_lbl_path):
    os.makedirs(val_lbl_path)

# 先开始随机打乱数据集,设置随机种子，保证每次打乱的顺序一样
spilt_factor = 0.4
random.seed(0)
random.shuffle(input_sar_path)
random.seed(0)
random.shuffle(input_opt_path)
random.seed(0)
random.shuffle(input_lbl_path)

border_idx = int(len(input_sar_path) * (1 - spilt_factor))  # int(len(input_sar_path)-500)#
print('border_idx=',border_idx)

# train
print('开始随机分割数据集')
print("train set")
for i in tqdm(range(0, border_idx),desc='train'):
    sar_name = os.path.basename(input_sar_path[i])
    opt_name = os.path.basename(input_opt_path[i])
    lbl_name = os.path.basename(input_lbl_path[i])

    sar_path = os.path.join(train_sar_path, sar_name)
    opt_path = os.path.join(train_opt_path, opt_name)
    lbl_path = os.path.join(train_lbl_path, lbl_name)


    copy(input_sar_path[i], sar_path)   #将文件从一个地方复制到另一个地方
    copy(input_opt_path[i], opt_path)
    copy(input_lbl_path[i], lbl_path)

# val
print("val set")
for i in tqdm(range(border_idx, border_idx + int(len(input_sar_path) * 0.2))):
    sar_name = os.path.basename(input_sar_path[i])
    opt_name = os.path.basename(input_opt_path[i])
    lbl_name = os.path.basename(input_lbl_path[i])

    sar_path = os.path.join(val_sar_path, sar_name)
    opt_path = os.path.join(val_opt_path, opt_name)
    lbl_path = os.path.join(val_lbl_path, lbl_name)

    copy(input_sar_path[i], sar_path)
    copy(input_opt_path[i], opt_path)
    copy(input_lbl_path[i], lbl_path)


# test
print("test set")
for i in tqdm(range(border_idx + int(len(input_sar_path) * 0.2), len(input_sar_path))):
    sar_name = os.path.basename(input_sar_path[i])
    opt_name = os.path.basename(input_opt_path[i])
    lbl_name = os.path.basename(input_lbl_path[i])

    sar_path = os.path.join(test_sar_path, sar_name)
    opt_path = os.path.join(test_opt_path, opt_name)
    lbl_path = os.path.join(test_lbl_path, lbl_name)

    copy(input_sar_path[i], sar_path)
    copy(input_opt_path[i], opt_path)
    copy(input_lbl_path[i], lbl_path)




