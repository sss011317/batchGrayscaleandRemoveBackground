import numpy as np
import matplotlib.pyplot as plt
from torch import nn,optim
from torch.autograd import Variable
import torch
import cv2
x_data = np.linspace(-2,2,200)[:,np.newaxis]
noise = np.random.normal(0,0.2,x_data.shape)
y_data = np.square(x_data) + noise

plt.scatter(x_data,y_data)
# plt.show()
# exit()
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
        #1-10-1
        self.fc1 = nn.Linear(1,10)
        self.tanh = nn.Tanh()
        self.fc2 = nn.Linear(10,1)
    def forward(self,x):
        x = self.fc1(x)
        x = self.tanh(x)
        x = self.fc2(x)
        return x

#定義模型
model = LinearRegression()
#定義代價函數
mse_loss = nn.MSELoss()
#優化模型 lr = 學習率
optimizer = optim.SGD(model.parameters(), lr=0.1) 
#參數查看
for name, parameters in model.named_parameters():
    print('name:{},parm:{}'.format(name,parameters))

for i in range(2001):
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
plt.plot(x_data.numpy(),y_pred.data.numpy(),'r-',lw=3)
plt.show()