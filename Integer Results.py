import math
import random
import numpy as np
import pandas as pd

class Results():
    def __init__(self,number):
        self.value = number
        self.count = 0

z = -1
while z <= 9:        
    ##count_bucket = np.arange(0,101) ##normal range
    count_bucket = np.arange(0,51) ##closest to 50 range
    results_bucket = []
    for y in count_bucket:
        results_bucket.append(Results(y))
    looper = 0
    while looper < 1000000:
        testrun = []
        rolls = 0
        if z < 0:
            while rolls <= abs(z):
                r = abs(50-random.randint(0,100))
                testrun.append(r)
                rolls += 1
            q = int(max(testrun))
        elif z == 0:
            q = abs(50-random.randint(0,100))
        elif z > 0:
            while rolls <= z:
                r = abs(50-random.randint(0,100))
                testrun.append(r)
                rolls += 1
            q = int(min(testrun))
        for x in results_bucket:
            if q == x.value:
                x.count += 1
        looper += 1
    output_file = pd.DataFrame([w.__dict__ for w in results_bucket])
    output_name = 'RollSpread_ClosestTo50_' + str(z)+".csv"
    output_file.to_csv(output_name,index=False)
    z += 1
    