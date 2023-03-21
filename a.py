import numpy as np
import os
import PIL
import random
import torch
import torchvision
from torchvision import transforms
import time

import torch
import argparse


img_opt_path = r'whu-opt-sar\crop\train\opt\NH49E001013_2.tif'
img_opt = PIL.Image.open(img_opt_path)
img_opt=torchvision.transforms.ToTensor()(img_opt)
a=transforms.ToPILImage()(img_opt)
print(img_opt.shape)
print(a.mode)
print(np.array(a)[:, :, :3].shape)
# a=transforms.ToTensor(img_opt)
# print(a.shape)
