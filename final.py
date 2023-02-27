import pandas as pd
from convert import *

url = "https://fbref.com/en/matches/3adf2aa7/Brentford-Arsenal-August-13-2021-Premier-League"
convert_outcome(url)

"""
get all url of 38weeks*10matches/week = 380 games of the season 21-22
"""
import requests
from bs4 import BeautifulSoup
#from menu generate all links to 
url = "https://fbref.com/en/comps/9/2021-2022/schedule/2021-2022-Premier-League-Scores-and-Fixtures"
page = requests.get(url)
soup = BeautifulSoup(page.content,"lxml")
leftonly = soup.find_all("td",attrs={"class":"left","data-stat":"match_report"})
leftiz = soup.find_all("td",attrs={"class":"left iz","data-stat":"match_report"})
r = [i for i in leftonly if i not in leftiz]
gamelist_url = []
for i in range(len(r)):
    myurl = "https://fbref.com"+r[i].find("a").get("href") 
    gamelist_url.append(myurl)

tryme = pd.concat([convert_outcome(gamelist_url[i]) for i in range(len(gamelist_url))],axis=1)

tryme