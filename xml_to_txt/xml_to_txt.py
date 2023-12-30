import os
import xml.etree.ElementTree as ET


Pascal_VOC2012_dict = {
    'aeroplane': 0,
    'bicycle': 1,
    'bird': 2,
    'boat': 3,
    'bottle': 4,
    'bus': 5,
    'car': 6,
    'cat': 7,
    'chair': 8,
    'cow': 9,
    'diningtable': 10,
    'dog': 11,
    'horse': 12,
    'motorbike': 13,
    'person': 14,
    'pottedplant': 15,
    'sheep': 16,
    'sofa': 17,
    'train': 18,
    'tvmonitor': 19
}


def xml_to_txt(xml_path, txt_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()


    with open(txt_path, 'w') as txt_file:
        width = float(root.find('size/width').text)
        height = float(root.find('size/height').text)

        for obj in root.findall('object'):
            name = obj.find('name').text
            bbox = obj.find('bndbox')
            xmin = float(bbox.find('xmin').text)
            ymin = float(bbox.find('ymin').text)
            xmax = float(bbox.find('xmax').text)
            ymax = float(bbox.find('ymax').text)
            txt_file.write(f"{Pascal_VOC2012_dict[name]} {xmin/width} {ymin/height} {xmax/width} {ymax/height}\n")


xml_folder_path = './Annotations'
txt_folder_path = './Annotations_txt'
for filename in os.listdir(xml_folder_path):
    if filename.endswith('.xml'):
        xml_file_path = os.path.join(xml_folder_path, filename)
        txt_file_path = os.path.join(txt_folder_path, filename.replace('.xml', '.txt'))

        xml_to_txt(xml_file_path, txt_file_path)