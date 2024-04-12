### Reproducibility (Trying to take random out of random)
### In short how a nreural networks learns: 
###"Starts with random numbers -> tensor operations-> update random numbers to try and make them better representations of the data-> again->again........"




import torch
random_tensor1 = torch.rand(3,4)
print(random_tensor1)
random_tensor2 = torch.rand(3,4)
print(random_tensor2)
print(random_tensor1 == random_tensor2)


### Lets makes some random but reproducible tensors
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
random_tensor3 = torch.rand(3,4)
torch.manual_seed(RANDOM_SEED)
random_tensor4 = torch.rand(3,4)
print(random_tensor3)
print(random_tensor4)
print(random_tensor3 == random_tensor4)
