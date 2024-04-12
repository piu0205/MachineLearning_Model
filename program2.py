import torch
scalar = torch.tensor(7)
print("The output:",scalar)
s = scalar.ndim
print (s)
count = scalar.item
print(count)


vector = torch.tensor([7,7])
print("The vector output:",vector)
v = vector.ndim
print(v)
sh = vector.shape
print(sh)


MATRIX = torch.tensor([[4,6],
                [7,8]])
        
print("Matrix is:",MATRIX)
m = MATRIX.ndim
print(m)
axis = MATRIX[1]
print(axis)
shape = MATRIX.shape
print("Shape of the matrix:",shape)

TENSOR = [[[4.,6.,9.],[9.,4.,8.],[2.,6.,4.]]]
my_tensor = torch.tensor(TENSOR)
print("The tensor is:",my_tensor)

random_tensor = torch.rand(4,6) 
print(random_tensor)
