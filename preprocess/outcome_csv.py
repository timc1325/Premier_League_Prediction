import time
import pandas as pd
import sys
if "convert" not in sys.path:
    #!!!path needs to change per user!!!
    sys.path.insert(0,"convert")

from convert_res import *
matches = pd.read_csv("data/match.csv")

start = time.time()
temptime= time.time()
for idx in range(0, matches.shape[0]):
    step = time.time()
    temp = pd.read_html(matches["url"][idx])
    #append information on the right of match csv: team name, score, formation?
    if (len(temp)<20):
        continue

    result = convert_outcome(temp[2])
    result.to_csv("data/outcome/"+str(idx)+".csv")

    print(time.time() -step,"  ",time.time() - start, idx)

    if idx % 20 == 19:
        sleepneed = 65-(time.time() - temptime)
        print("Now Sleeping for ",sleepneed," seconds zZZ...")
        time.sleep(sleepneed)
        temptime = time.time()