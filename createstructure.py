from scipy.io import loadmat
import pandas as pd
import os
import shutil

TRAIN_IMG_DIR = "/home/thariq/stanford_cars/train/"
VAL_IMG_DIR = "/home/thariq/stanford_cars/val/"


for idx in range(matrix['class_names'].shape[1]):
    os.makedirs(TRAIN_IMG_DIR+str(idx+1))

for idx,train_file in enumerate(train_addrs):
    shutil.copy2(train_file,os.path.join(TRAIN_IMG_DIR,str(train_labels[idx])))

for idx,val_file in enumerate(val_addrs):
    shutil.copy2(val_file,os.path.join(VAL_IMG_DIR,str(val_labels[idx])))

