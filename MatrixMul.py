### Element wise multiplication 
import torch 
tensor = torch.tensor([4,5,6])
print(tensor)
mul = tensor * tensor
print(f"Element wise multiplication=",mul)

### Matrix Multiplication 
A = torch.tensor([[4,5],
                  [8,5]]) 

B = torch.tensor([[8,6],
                 [3,4]])
result = torch.matmul(A,B)
print("Matrix Multiplication is: ",result)


A = torch.tensor([[4,5,6],
                  [8,5,7]]) 

B = torch.tensor([[8,6,8],
                 [3,4,7],
                 [6,4,5]])
result1 = torch.matmul(A,B)
print("Matrix Multiplication is: ",result1)