import numpy as np

coffee = np.array([2,2,3,5,7,9,10,15,16])

coffee.mean() 
np.median(coffee) 

coffee_q1 = np.array([2,2,3,5])
coffee_q3 = np.array([9,10,15,16])

q1_median = np.median(coffee_q1)
q3_median = np.median(coffee_q3)

IQR = q3_median - q1_median

print(q1_median)
print(q3_median)
print(IQR)