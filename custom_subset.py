# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:08:15 2021

@author: Vinit
"""

import os
import shutil
import csv
import pandas as pd
import numpy as np
import time
from tqdm import tqdm


start_time = time.time()




current_path = os.getcwd() # get path where this file is
print("\nCurrent path = "+ current_path + "\n")

images_folder = current_path + "/PASCAL_VOC/images"
labels_folder = current_path + "/PASCAL_VOC/labels"
new_labels_folder = current_path + "/PASCAL_VOC/custom_labels"

train_file = current_path + "/PASCAL_VOC/train.csv"
test_file = current_path + "/PASCAL_VOC/test.csv"
custom_train = current_path + "/PASCAL_VOC/custom_train.csv"
custom_test =current_path + "/PASCAL_VOC/custom_test.csv"

if not os.path.exists(new_labels_folder):
    os.mkdir(new_labels_folder)


f_train = open(custom_train,'w')
f_test = open(custom_test,'w')
writer_train = csv.writer(f_train)
writer_test = csv.writer(f_test)

PASCAL_CLASSES = [
    "aeroplane",
    "bicycle",
    "bird",
    "boat",
    "bottle",
    "bus",
    "car",
    "cat",
    "chair",
    "cow",
    "diningtable",
    "dog",
    "horse",
    "motorbike",
    "person",
    "pottedplant",
    "sheep",
    "sofa",
    "train",
    "tvmonitor"
]

### make sure the spelling is similar to the one in PASCAL_CLASSES list
custom_classes = ["bottle","person","tvmonitor"]  
print("The labels of your custom class is as follows : {} and it contains {} classes \n"
      .format(custom_classes,len(custom_classes)))

# just to check if custom class lies in PASCAL dataset
for i in custom_classes:
    exist_count = PASCAL_CLASSES.count(i)
    assert exist_count > 0, "The class in custom class list does not exist in PASCAL_CLASSES"

#index of custom_classes in Pascal_data
og_indexing = []
new_indexing = []

for _class in custom_classes:
    #new_indexing.append(custom_classes.index(_class))
    og_indexing.append(PASCAL_CLASSES.index(_class))
    
print(og_indexing)
#print(new_indexing)
    
c = os.listdir(labels_folder)


data = pd.read_csv(train_file, header=None)

list_text = data[1]

for i in tqdm(range(len(list_text))):
    path = os.path.join(labels_folder, str(list_text[i]))
    text_value = pd.read_csv(path, delimiter=(" "),header=None)
    labels = np.array(text_value[0])
    #for _ in range(len(labels)):
    indexes = []
    for j in og_indexing:
        indexes.append(list(np.where(labels == j)[0]))
        
    if indexes != [[],[],[]]:
        _string = data.loc[[i],0:].to_string(index=False, header=False).split()
        writer_train.writerow(_string)
        for m in range(len(indexes)):
            for n in indexes[m]:
                new_label = open(os.path.join(new_labels_folder, list_text[i]),'a')
                new_label.write('{} {}\n'.format(m,text_value.iloc[[n], 1:].to_string(index=False,header=False)))       
                new_label.close()
    
data = pd.read_csv(test_file, header=None)

list_text = data[1]

for i in tqdm(range(len(list_text))):
    path = os.path.join(labels_folder, str(list_text[i]))
    text_value = pd.read_csv(path, delimiter=(" "),header=None)
    labels = np.array(text_value[0])
    #for _ in range(len(labels)):
    indexes = []
    for j in og_indexing:
        indexes.append(list(np.where(labels == j)[0]))
        
    if indexes != [[],[],[]]:
        _string = data.loc[[i],0:].to_string(index=False, header=False).split()
        writer_test.writerow(_string)
        #print(new_data)
        for m in range(len(indexes)):
            for n in indexes[m]:
                new_label = open(os.path.join(new_labels_folder, list_text[i]),'a')
                new_label.write('{} {}\n'.format(m,text_value.iloc[[n], 1:].to_string(index=False,header=False)))       
                new_label.close()
                


f_train.close()
f_test.close()
print("--- %s seconds ---" % (time.time() - start_time))

print('\nSuccessfully DONE')