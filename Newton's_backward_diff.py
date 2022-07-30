

#First derivative by Newton's backward difference
import numpy as np
xs,h=np.linspace(1,6,6,retstep=True)
ys=np.array([2.7183,3.3210,4.0552,4.9530,6.0496,7.3891])
yrs=np.flipud(ys)
s=0.0
k=0
for i in np.arange(len(ys),1,-1):
    yrs=-np.diff(yrs)
    s+=yrs[0]/(k+1)
    k+=1
print("first derivative: ",s/h)


'''
Difference: At f'(x=6) , since it is a backward difference method
[[1.3395 1.0966 0.8978 0.7342 0.6027]
[0.2429 0.1988 0.1636 0.1315]
[0.0441 0.0352 0.0321]
[0.0089 0.0031]
[0.0058]]
The answer is:
first derivative:  1.4790350000000019
'''
