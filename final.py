import sys
if "/Users/tc/Premier_League_Prediction/convert" not in sys.path:
    #!!!path needs to change per user!!!
    sys.path.insert(0,"/Users/tc/Premier_League_Prediction/convert")
from convert_res import *
import pandas as pd
import time
import random

start= time.time()
urls = pd.read_csv("data/total.csv").iloc[:,1]
for i in range(19):
    a = random.randint(0,9000)
    convert_outcome(urls[a])
    print(a, time.time()-start)
(time.time()-start)/19
