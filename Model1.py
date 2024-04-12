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
W = (X[:10], Y[:10])
print(W)



### Create a train/test splits 
train_split = int(0.8 * len(X))
X_train, Y_train = X[:train_split], Y[:train_split]
X_test, Y_test = X[train_split:], Y[train_split:]
a = len(X_train)
print(a)
b = len(Y_train)
print(b)
c = len(X_test)
print(c)
d = len(Y_test)
print(d)

def plot_predictions(train_data=X_train,
                     train_label=Y_train,
                     test_data=X_test,
                     test_label=Y_test,
                     predictions=None):

 plt.figure(figsize=(10, 7))
### PLotting training data in blue 
 plt.scatter(train_data, train_label, c="b", s=4, label="Trainig Data")

### PLotting test data in blue 
 plt.scatter(test_data, test_label, c="g", s=4, label="Testing Data")

### Are there any predictions?
 if predictions is not None: 
    plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")

 plt.legend(prop={"size": 14});

plot_predictions();
plt.show()