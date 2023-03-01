import sys
if "/Users/tc/Premier_League_Prediction/convert" not in sys.path:
    sys.path.insert(0,"/Users/tc/Premier_League_Prediction/convert")
from convert_outcome import *
from formation import *
import pandas as pd
import time
import random

start= time.time()
urls = pd.read_csv("data/total.csv").iloc[:,1]
urls[100]
a = pd.read_html(urls[100])[2].drop([1,3,5,7],axis=0).fillna(0).reset_index(drop=True)
a
option,order=1,1
a.iloc[option,:][order].split()[0-order]
c,p=-1,0
result = int(a.iloc[option,:][order].split()[c])
temp =  a.iloc[option,:][order].split()[p].strip("%")
result,temp
convert_outcome(urls[100])
