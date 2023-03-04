import sys
if "convert" not in sys.path:
    #!!!path needs to change per user!!!
    sys.path.insert(0,"convert")

import pandas as pd
import time
import pickle
import pandas as pd
from convert_res import *
from Classes import *

with open("data/namelist.pkl", "rb") as inp:
    namelist = pickle.load(inp)
inp.close()
"""
need change argument of function
"""
start= time.time()
matches = pd.read_csv("data/match.csv")
#try one game gather training data
mymatch = matches.iloc[5,:]
mydate = mymatch["Date"]
mymatch20tables = pd.read_html(mymatch["url"])
convert_outcome(mymatch20tables[2]).iloc[0,0] #outcome posession

#outcome posession



    




