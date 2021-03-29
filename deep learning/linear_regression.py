import numpy as np
import matplotlib.pyplot as plt
from torch import nn,optim
from torch.autograd import Variable
import torch
import cv2
x_data = np.random.rand(100)
noise = np.random.normal(0,0.01,x_data.shape)
y_data = x_data*0.1 + 0.2 + noise
plt.scatter(x_data,y_data)
# plt.show()
#二維
x_data = x_data.reshape(-1,1)
y_data = y_data.reshape(-1,1)
#把numpy變成tensor
x_data = torch.FloatTensor(x_data)
y_data = torch.FloatTensor(y_data)
inputs = Variable(x_data)
target = Variable(y_data)
#創建神經網路模型
class LinearRegression(nn.Module):
    
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.fc = nn.Linear(1,1)
    def forward(self,x):
        out = self.fc(x)
        return out

#定義模型
model = LinearRegression()
#定義代價函數
mse_loss = nn.MSELoss()
#優化模型
optimizer = optim.SGD(model.parameters(), lr=0.1) 
#參數查看
# for name, parameters in model.named_parameters():
    # print('name:{},parm:{}'.format(name,parameters))

for i in range(1001):
    out = model(inputs)
    #計算loss
    loss = mse_loss(out,target)
    #梯度清0
    optimizer.zero_grad()
    #計算梯度
    loss.backward()
    #修改權值
    optimizer.step()
    if i%200 == 0:
        print(i,loss.item())

y_pred = model(inputs)
plt.scatter(x_data,y_data)
# print()
plt.plot(x_data.numpy(),y_pred.data.numpy(),'r-',lw=3)
plt.show()