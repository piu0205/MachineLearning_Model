# Create a tensor 
import torch
some_tensor = torch.rand(3,4)
print(some_tensor)

# Find out details about spome tensor
print(some_tensor)
print(f"Datatype of tensor: {some_tensor.dtype}")
print(f"Shape of the tensor: {some_tensor.shape}")
print(f"Device of the tensor: {some_tensor.device}")

### Manipulating Tensors (tensor operations)
### Tensor operations include: Addition, Subtraction, Multiplication, Division, Matrix Multiplication,


# Firts create a tensor
tensor = torch.tensor([3, 4, 5])
t_add = tensor + 10
print(t_add)

# Multiply tensor by 10
tensor = tensor * 10
print(tensor)

# Subtraction tensor 
sub = tensor - 10
print(sub)

# Try out PyTorch in-built functions 
mul = torch.mul(tensor,10)
print(mul)