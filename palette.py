from PIL import Image
import numpy as np

# palette = [0, 200, 0,
#            150, 250, 0,
#            150, 200, 150,
#            200, 0, 200,
#            150, 0, 250,
#            150, 150, 250,
#            250, 200, 0,
#            200, 200, 0,
#            200, 0, 0,
#            250, 0, 150,
#            200, 150, 150,
#            250, 150, 150,
#            0, 0, 200,
#            0, 150, 200,
#            0, 200, 250,
#            0, 0, 0]
palette = [0, 200, 0,
           150, 250, 0,
           150, 200, 150,
           200, 0, 200,
           150, 0, 250,
           150, 150, 250,
           250, 200, 0,
           200, 200, 0,
           200, 0, 0,
           250, 0, 150,
           200, 150, 150,
           250, 150, 150,
           0, 0, 200,
           0, 150, 200,
           0, 200, 250,
           0, 0, 0]
#print(len(palette))  #48
zero_pad = 256 * 3 - len(palette)
#print(zero_pad)   #720
for i in range(zero_pad):
    palette.append(0)
# 将grey mask转化为彩色mask
#print(len(palette))  #768

#palette 是一个包含256个RGB值的列表

def colorize_mask(mask):
    mask_color = Image.fromarray(mask.astype(np.uint8)).convert('P')
    mask_color.putpalette(palette)
    return mask_color