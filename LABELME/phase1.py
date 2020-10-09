"""
original name: xml_labelme.py
date: 2020/10/08
written by KatoMori
purpose: labelmeデータセットを分析し,labelname'car'の写真とxmlファイルを選別,別ディレクトリへコピー
"""

import xml.etree.ElementTree as ET
import os
import shutil

# PATH = labelmeデータセットへのPATH
DIR_NAME = 'labelme/'
PATH = './' + DIR_NAME

DIR_IMG_NAME = 'Images/'
DIR_ANN_NAME = 'Annotations/'
ANN_PATH = PATH + DIR_ANN_NAME
IMG_PATH = PATH + DIR_IMG_NAME

# _DIR_NAME = 選別された画像,xmlのコピー先
COPY_DIR_NAME = 'phase1/'
COPY_PATH = PATH + COPY_DIR_NAME

file_list = os.listdir(PATH)
number = 1

label_list = ['car', 'van', 'truck', 'bus']
def analyze_xml(root, file, number, ANN_DIR_PATH, IMG_DIR_PATH):
    # print(ANN_DIR_PATH + file[0] + '.xml')
    # print("analyze")
    for object in root.iter('object'):
        for label_name in object.iter('name'):
            label_name = label_name.text
            label_name = label_name.split('\n')
            label_name = label_name[1]
            if label_name in label_list:
                # print("car")
                # print(COPY_PATH)
                shutil.copy(ANN_DIR_PATH + file[0] + '.xml', COPY_PATH+str(number)+'.xml')
                shutil.copy(IMG_DIR_PATH + file[0] + '.jpg', COPY_PATH + str(number) + '.jpg')
                # print("copied")
                number += 1
                return number
            else:
                #print("no car!")
                continue
    return number


# main()
def order(number):
    ann_list = os.listdir(ANN_PATH)
    # print(ann_list)
    # print(len(ann_list))
    for dir_name in ann_list:
        ANN_DIR_PATH = ANN_PATH + dir_name + '/'
        IMG_DIR_PATH = IMG_PATH + dir_name + '/'
        file_list = os.listdir(ANN_DIR_PATH)
        for file_name in file_list:
            file = file_name.split('.')
            if file[1] == 'xml':
                # print(ANN_DIR_PATH + file_name)
                try:
                    tree = ET.parse(ANN_DIR_PATH + file_name)
                    root = tree.getroot()
                    number = analyze_xml(root, file, number, ANN_DIR_PATH, IMG_DIR_PATH)
                    # print("number:", end=' ')
                    # print(number)
                except:
                    # print("except")
                    continue


"""
if __name__ == '__main__':
    ann_list = os.listdir(ANN_PATH)
    for dir_name in ann_list:
        ANN_DIR_PATH = ANN_PATH + dir_name + '/'
        IMG_DIR_PATH = IMG_PATH + dir_name + '/'
        file_list = os.listdir(ANN_DIR_PATH)
        for file_name in file_list:
            file = file_name.split('.')
            if file[1] == 'xml':
                print(ANN_DIR_PATH + file_name)
                try:
                    tree = ET.parse(ANN_DIR_PATH + file_name)
                    print(tree)
                    root = tree.getroot()
                    print(root)
                    number = analyze_xml(root, file, number, ANN_DIR_PATH, IMG_DIR_PATH)
                except:
                    continue
"""








