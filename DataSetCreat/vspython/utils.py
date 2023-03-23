from PIL import Image
import math,os
from xml.etree import ElementTree as ET
import json

def keep_image_size_open(path, size=(256, 256)):
    img = Image.open(path)
    temp = max(img.size)
    mask = Image.new('RGB', (temp, temp), (0, 0, 0))
    mask.paste(img, (0, 0))
    mask = mask.resize(size)
    return mask


def make_data_center_txt(xml_dir):
    with open('data_center.txt', 'a') as f:
        f.truncate(0)
        path=r'data/images'
        xml_names = os.listdir(xml_dir)
        for xml in xml_names:
            xml_path = os.path.join(xml_dir, xml)
            in_file = open(xml_path)
            tree = ET.parse(in_file)
            root = tree.getroot()
            image_path = root.find('path')
            polygon = root.find('outputs/object/item/polygon')
            data = []
            c_data = []
            data_str = ''
            print(xml)
            for i in polygon:
                data.append(int(i.text))
                data_str = data_str + ' ' + str(i.text)
            for i in range(0, len(data), 2):
                c_data.append((data[i], data[i + 1]))
            data_str = os.path.join(path,image_path.text.split('\\')[-1]) +data_str
            f.write(data_str + '\n')


if __name__ == '__main__':
    make_data_center_txt('data/xml')