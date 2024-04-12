import torch
from torch import nn
import matplotlib.pyplot as plt 

### we will use a linear regression formula to make a straight line 

weight = 0.7
bias = 0.3  
start = 0
end = 1
step = 0.02
X = torch.arange(start,end,step).unsqueeze(dim = 1)
Y = weight * X + bias
plt.plot(X[:10], Y[:10])
plt.show()
