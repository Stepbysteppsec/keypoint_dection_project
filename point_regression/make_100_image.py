import os

import cv2

path= 'data/images'
index=0
for i in os.listdir(path):
    img=cv2.imread(os.path.join(path,i))
    out=cv2.resize(img,(100,100))
    cv2.imwrite(f'out/{index}.png',out)
    index+=1

