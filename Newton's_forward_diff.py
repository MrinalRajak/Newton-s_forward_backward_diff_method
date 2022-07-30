

#First derivative by Newton's forward difference

import numpy as np
x=np.array([1,2,3,4,5,6],dtype=float)
y=np.array([2.7183,3.3210,4.0552,4.9530,6.0496,7.3891],dtype=float)
h=1.0
s=0.0
k=0
for i in np.arange(len(y),1,-1):
    y=np.diff(y)
    s+=(-1)**k*y[0]/(k+1)
    k+=1
print("First derivative: ",s/h)
'''
Difference:   At f'(x=1),since it is a forward difference method
[[0.6027 0.7342 0.8978 1.0966 1.3395]
[0.1315 0.1636 0.1988 0.2429]
[0.0321 0.0352 0.0441]
[0.0031 0.0089]
[0.0058]]
The answer is:
First derivative:  0.5480350000000009
'''
