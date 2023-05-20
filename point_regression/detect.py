import os

import torch
from PIL import Image,ImageDraw
from dataset import *
from net import *

path='test_image'
net=Net()
net.load_state_dict(torch.load('params/net.pth'))
net.eval()
for i in os.listdir(path):
    img=Image.open(os.path.join(path,i))
    draw=ImageDraw.Draw(img)
    img_data=tf(img)
    img_data=torch.unsqueeze(img_data,dim=0)
    out=net(img_data)
    out=(out[0]*100).tolist()
    for j in range(0,len(out),2):
        draw.ellipse((out[j]-2,out[j+1]-2,out[j]+2,out[j+1]+2),(255,0,0))
    img.show()

