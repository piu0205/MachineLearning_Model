### Reshaping 
import torch
x = torch.arange(1.,10.)
print(x, x.shape)

x_reshaped = x.reshape(1,9)
print(x_reshaped, x_reshaped.shape)

x_reshaped = x.reshape(1,9)
print(x_reshaped, x_reshaped.shape)

### Change the view 
### [View just show a diffrent variable of a tensor]
z = x.view(1,9)
print(z.shape)

z[:, 0] = 5
print(z,x) 

### Stack tensors on top 
x_stacked = torch.stack([x, x, x, x], dim=0)
print(x_stacked) 


### Squeeze and Unsqueeze
### torch.squeezde(): Squeezes all one dimensions from the tareget tensors

x = torch.zeros(2, 1, 2, 1, 2)
print(x.size())
y = torch.squeeze(x)
print(y.size())
y = torch.squeeze(x, 0)
print(y.size())
y = torch.squeeze(x, 1)
print( y.size())
y = torch.squeeze(x, (1, 2, 3))
