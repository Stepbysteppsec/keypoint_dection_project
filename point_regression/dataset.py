import os
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image

tf = transforms.Compose([
    transforms.Resize((50, 50)),
    transforms.ToTensor()
])

class MyDataset(Dataset):
    def __init__(self, root):
        f = open(root, 'r')
        self.dataset = f.readlines()

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        parts = self.dataset[index].split()
        img_path = os.path.abspath(parts[0])
        img_data = Image.open(img_path)
        original_size = img_data.size
        img_data = tf(img_data)
        resize_w = original_size[0] / 50 # 计算宽度缩放比例
        resize_h = original_size[1] / 50 # 计算高度缩放比例
        points = parts[1:5]
        points = [int(i) / resize_w if index % 2 == 0 else int(i) / resize_h for index, i in enumerate(points)] # 对关键点坐标进行缩放操作
        return img_data, points
    
if __name__ == '__main__':
    data = MyDataset(
        r'/Users/lidenghui/pythonProject/keypoint_detection_project/dataFolder/data_center_5.txt')

    for i in data:
        i
#     data = MyDataset('keypoint_detection_project/dataFolder/data_center_5.txt')
#     for i in data:
