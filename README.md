## Custom_VOC for YOLO versions

##### Please download the Pascal VOC dataset in YOLO annotation format

https://www.kaggle.com/aladdinpersson/pascal-voc-dataset-used-in-yolov3-video

##### unzip the folder (PASCAL_VOC) and place it near your custom_subset.py file

##### please write the classes you want the custom dataset for in the custom_classes list in the custom_subset.py file

##### This will create a new folder named custom label where the new annotations based on custom classes are saved
The main work of this code lies here! As originally this dataset has 20 classes, hence the labels are numbered from 0 till 19. To create a subset of this dataset means that this annotations should also be changed (labels inside the annotation).
There are 2 more files created namely, custom_train.csv and custom_test.csv which will be used to load data in the DataLoader. 
A new copy of these custom class images is not created, so as to safe space as we already have the entire dataset and the path of the custom classes is written in custom_train.csv
