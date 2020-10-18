"""
date: 2020/10/08
written by KatoMori
purpose: object detection api用のxmlファイルを作成
"""
import xml.etree.ElementTree as ET


def sub_element(parent, name, text):
    element = ET.SubElement(parent,name)
    element.text = text
    return element


def xml_write(number, img_shape, point_list, EXPORT_PATH):
    # print("called")
    annotation = ET.Element('annotation')
    tree = ET.ElementTree(element=annotation)
    folder = sub_element(annotation, 'folder', 'images')
    filename = sub_element(annotation, 'filename', number + '.jpg')

    source = ET.SubElement(annotation, 'source')
    database = sub_element(source, 'database', 'Unknown')

    size = ET.SubElement(annotation, 'size')
    width = sub_element(size, 'width', str(img_shape[0]))
    height = sub_element(size, 'height', str(img_shape[1]))
    depth = sub_element(size, 'depth', str(img_shape[2]))

    segmented = sub_element(annotation, 'segmented', '0')

    for dict in point_list:
        # print(dict)
        object = ET.SubElement(annotation, 'object')
        name = sub_element(object, 'name', dict['label'])  # 変更 小路 'car'
        pose = sub_element(object, 'pose', 'Unspecified')
        truncated = sub_element(object, 'truncated', '0')
        difficult = sub_element(object, 'difficult', '0')

        bndbox = ET.SubElement(object, 'bndbox')
        xmin = sub_element(bndbox, 'xmin', dict['xmin'])
        ymin = sub_element(bndbox, 'ymin', dict['ymin'])
        xmax = sub_element(bndbox, 'xmax', dict['xmax'])
        ymax = sub_element(bndbox, 'ymax', dict['ymax'])

    tree.write('./' + EXPORT_PATH + number + '.xml', encoding='utf-8', xml_declaration=True)
