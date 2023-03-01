#Currently Unused
import pandas as pd
import re

def get_formation(url) -> tuple:
    home_formation = re.findall("\((.+)\)",pd.read_html(url)[0].columns[0])[0]
    away_formation = re.findall("\((.+)\)",pd.read_html(url)[1].columns[0])[0]
    return home_formation,away_formation

