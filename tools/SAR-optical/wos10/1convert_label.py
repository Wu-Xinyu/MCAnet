import numpy as np
import glob, os, h5py
import os
import cv2
from scipy import misc
from PIL import Image

Image.MAX_IMAGE_PIXELS = None


def old_label2new_label(lbl, root_path, name):
    h, w = lbl.shape
    print(np.where(lbl == 0))

    lbl[np.where(lbl == 0)] = 0   #lbl是一个二维数组，np.where(lbl == 0)返回的是一个元组，元组中的第一个元素是满足条件的行号，第二个元素是满足条件的列号
    lbl[np.where(lbl == 10)] = 1
    lbl[np.where(lbl == 20)] = 2
    lbl[np.where(lbl == 30)] = 3
    lbl[np.where(lbl== 40)] = 4
    lbl[np.where(lbl == 50)] = 5
    lbl[np.where(lbl == 60)] = 6
    lbl[np.where(lbl == 70)] = 7

    path = os.path.join(root_path, name)
    print('=====> save', path)
    Image.fromarray(np.uint8(lbl[:, :])).convert('L').save(path)

    return

if __name__ == '__main__':


    lbl_root = r'whu-opt-sar\\lbl'
    new_lbl_root = r'whu-opt-sar\\newlbl'

    label_files = sorted(os.listdir(lbl_root))
    for file_name in label_files:
        data = np.array(Image.open(os.path.join(lbl_root, file_name)))
        old_label2new_label(data, new_lbl_root, file_name)



