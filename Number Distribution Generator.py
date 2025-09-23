import random
import math
import pandas as pd
import numpy as np

class NumberBucket():
    def __init__(self,value):
        self.value = round(int(value * 1000)/1000,2)
        self.count = 0

numberbucket = np.arange(0.00,25.00,0.01).tolist()
Number_Bucket = []
for k in numberbucket:
    j = NumberBucket(k)
    Number_Bucket.append(j)
number_list = []

print("Number Bucket Generated")
count = 0
while count < 10000000:
    x = np.random.normal(0,5)
    x *= 1000
    z = int(x)
    z /= 1000
    z -= 0.5
    # x = random.random()
    # x -= 0.5
    # x *= 4
    # x **= 2
    # x *= 5
    y = round(abs(z),2)
    number_list.append(y)
    for k in Number_Bucket:
        if y == k.value:
            k.count += 1
            break
    count += 1
number_list.sort()
print("Random Numbers Generated")
df = pd.DataFrame([vars(b) for b in Number_Bucket])
df.to_csv('number_generator.csv',index=False)
dx = pd.DataFrame(number_list)
dx.to_csv('number_generator_list.csv',index=False)