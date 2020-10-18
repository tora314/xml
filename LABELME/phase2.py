"""
original name: car_filt.py
date: 2020/10/08
written by KatoMori
purpose: labelmeのannotationsデータをobject detection api用にexport
"""

import xml.etree.ElementTree as ET
import os
import shutil
import ano
import cv2

PATH = './' + 'labelme/'

# exportされるデータ群
DIR_NAME = 'phase1/'
DIR_PATH = PATH + DIR_NAME

# export先
EXPORT_DIR_NAME = 'phase2/'
EXPORT_PATH = PATH + EXPORT_DIR_NAME
label_list = ['van', 'truck', 'bus']


def xml_to_str(xml_name):
    word = xml_name.text
    word = word.split('\n')
    word = word[1]
    return word


def min_max_point(x_list,y_list):
    point_dict = {}
    point_dict['xmin'] = str(min(x_list))
    point_dict['xmax'] = str(max(x_list))
    point_dict['ymin'] = str(min(y_list))
    point_dict['ymax'] = str(max(y_list))
    return point_dict


def analyze_point(root):
    point_list = []
    for object in root.iter('object'):
        x_list = []
        y_list = []
        for label_name in object.iter('name'):
            label = xml_to_str(label_name)
            if label in label_list:
                # print("car")
                for polygon in object.iter('polygon'):
                    # print("polygon")
                    for pt in polygon.iter('pt'):
                        # print("pt")
                        for x in pt.iter('x'):
                            x_list.append(int(xml_to_str(x)))
                        for y in pt.iter('y'):
                            y_list.append(int(xml_to_str(y)))
                    point_dict = min_max_point(x_list, y_list)
                    point_dict['label'] = label  # 変更 小路
                    point_list.append(point_dict)
            else:
                #print("no car!")
                continue
    return point_list


def order(number):
    file_list = os.listdir(DIR_PATH)
    for file_name in file_list:
        file = file_name.split('.')
        if file[1] == 'xml':
            # print(ANN_DIR_PATH + file_name)
            try:
                tree = ET.parse(DIR_PATH + file_name)
                root = tree.getroot()
                point_list = analyze_point(root)
                img = DIR_PATH + file[0] + '.jpg'
                img = cv2.imread(img)
                img_shape = img.shape
                ano.xml_write(str(number), img_shape, point_list, EXPORT_PATH)
                shutil.copy(DIR_PATH + file[0] + '.jpg', EXPORT_PATH + str(number) + '.jpg')
                number = number + 1
            except:
                continue


"""
if __name__ == '__main__':
    file_list = os.listdir(DIR_PATH)
    number = 1
    for file_name in file_list:
        file = file_name.split('.')
        if file[1] == 'xml':
            # print(ANN_DIR_PATH + file_name)
            try:
                print(DIR_PATH+file_name)
                tree = ET.parse(DIR_PATH + file_name)
                root = tree.getroot()
                point_list = analyze_point(root)
                print(point_list)
                img = DIR_PATH + file[0] + '.jpg'
                print(img)
                img = cv2.imread(img)
                img_shape = img.shape
                print(img_shape)
                print(img_shape[0])
                ano.xml_write(str(number), img_shape, point_list, EXPORT_PATH)
                shutil.copy(DIR_PATH + file[0] + '.jpg', EXPORT_PATH + str(number) + '.jpg')
                number = number + 1
            except:
                continue
"""






