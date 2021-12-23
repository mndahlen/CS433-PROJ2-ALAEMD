import cv2
import numpy as np
import pandas as pd
import os

# Custom imports
from helpers import get_bbox

## To avoid overwriting ##
save = False
##########################

DATADIR = "data/kaggle"
DIRS = ["3003","3004","3022","3023"]

def get_bbox(im):
    # Get bbox of image (We expect everything but lego to be black, i.e 0 intensity)
    im_1_channel = np.sum(im,2)
    im_find_x = np.sum(im_1_channel,0)
    im_find_y = np.sum(im_1_channel,1)

    x_low = 0
    x_high = im.shape[1]
    y_low = 0
    y_high = im.shape[0]

    idx = 0
    low_found = False
    for i in im_find_x:
        if not low_found:
            if i != 0:
                low_found = True
                x_low = idx
        else:
            if i == 0:
                x_high = idx
                break
        idx += 1

    idx = 0
    low_found = False
    for i in im_find_y:
        if not low_found:
            if i != 0:
                low_found = True
                y_low = idx
        else:
            if i == 0:
                y_high = idx
                break
        idx += 1

    return (x_low,y_low,x_high,y_high)
'''
bbox_frame = pd.DataFrame(columns=["filename","label","x_low","y_low","x_high","y_high"])
for dir in DIRS:
    for filename in os.listdir(os.path.join(DATADIR,dir)):
        if filename.endswith(".png"): 
            print("dir:{}, file:{}".format(dir,filename))
            img = cv2.imread(os.path.join(DATADIR,dir,filename))
            bbox = get_bbox(img)
            bbox_frame = bbox_frame.append({"filename":filename,"label":dir,
                                            "x_low":bbox[0],"y_low":bbox[1],
                                            "x_high":bbox[2],"y_high":bbox[3]}, ignore_index=True)

# Add also all raw images
RAW_DIRS = ["2540", "3001", "3003", "3004", "3020", "3021", "3022", "3023", "3039", "3660"]
RAW_DATADIR = "data/raw_bricks"
for dir in RAW_DIRS:
    for filename in os.listdir(os.path.join(RAW_DATADIR,dir)):
        if filename.endswith(".png"): 
            print("dir:{}, file:{}".format(dir,filename))
            img = cv2.imread(os.path.join(RAW_DATADIR,dir,filename))
            bbox = get_bbox(img)
            bbox_frame = bbox_frame.append({"filename":filename,"label":dir,
                                            "x_low":bbox[0],"y_low":bbox[1],
                                            "x_high":bbox[2],"y_high":bbox[3]}, ignore_index=True)

if save:
    bbox_frame.to_csv("data/test/kaggle_bbox.csv", index=False)

'''