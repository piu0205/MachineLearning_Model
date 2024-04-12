import torch
from torch import nn 
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.rand(1,
                                              requires_grad=True,
                                              dtype=torch.float))
        self.bias = nn.Parameter(torch.rand(1,
                                              requires_grad=True,
                                              dtype=torch.float))
        
def forward(self, x: torch.Tensor) -> torch.Tensor:
    return self.weights * x + self.bias