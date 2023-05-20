import os

from torch import nn,optim
import torch
from dataset import *
from net import *
from torch.utils.data import DataLoader


if __name__ == '__main__':
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net=Net().to(device)
    weights='params/net.pth'
    if os.path.exists(weights):
        net.load_state_dict(torch.load(weights))
        print('loading successfully')
    opt=optim.Adam(net.parameters())
    loss_fun=nn.MSELoss()
    dataset=MyDataset('data_center.txt')
    data_loader=DataLoader(dataset,batch_size=2,shuffle=True)
    epoch = 1
    while True:
        for i,(image,label) in enumerate(data_loader):
            image,label=image.to(device),label.to(device)

            out=net(image)
            train_loss=loss_fun(out,label)

            print(f'{epoch}-{i}-train_loss:{train_loss.item()}')

            opt.zero_grad()
            train_loss.backward()
            opt.step()
        if epoch%10==0:
            torch.save(net.state_dict(),f'params/net.pth')
            print('save successfully')
        epoch+=1

