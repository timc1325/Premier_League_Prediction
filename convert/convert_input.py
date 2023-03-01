import pandas as pd
pd.set_option('display.max_columns', 32)
file = pd.read_csv("/Users/tc/Premier_League_Prediction/data/temp.csv",header=1)

file.drop(file.shape[0]-1,axis=0)
def convert_position(s: str):
    s= str(s)
    if s =="MF":
        s = "M"
    elif s=="DF":
        s = "B"
    else:
        s = s[-1]
    return s
    
file["Pos"]=file["Pos"].transform(convert_position)
file

