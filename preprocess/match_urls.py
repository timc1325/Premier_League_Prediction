"""
get all urls of 38 weeks * 10 matches/week * 5 leagues  = 380 games of 5 major leagues from 17-18 to 21-22 season(5 seasons)
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

start = time.time()
#from menu generate all links to each year's premier league starting 2008 up till today
gamelist_url = []
league =[(9,"Premier-League"),(12,"La-Liga"),(20,"Bundesliga"),(11,"Serie-A"),(13,"League-1")]

temp=0
for year in range(2017,2022):
        yearr = str(year)+"-"+str(year+1)
        for t1,t2 in league:
                url = "https://fbref.com/en/comps/"+str(t1)+"/"+yearr+"/schedule/"+yearr+"-"+t2+"-Scores-and-Fixtures"
                page = requests.get(url)
                soup = BeautifulSoup(page.content,"lxml")
                leftonly = soup.find_all("td",attrs={"class":"left","data-stat":"match_report"})
                leftiz = soup.find_all("td",attrs={"class":"left iz","data-stat":"match_report"})
                r = [i for i in leftonly if i not in leftiz]
                for i in range(len(r)):
                        myurl = "https://fbref.com"+r[i].find("a").get("href") 
                        if myurl not in gamelist_url and "Play-offs" not in myurl:
                                gamelist_url.append(myurl)
                time.sleep(3)
                print(time.time()-start, yearr, t2,len(gamelist_url)-temp)
                temp = len(gamelist_url)

pd.DataFrame(gamelist_url).to_csv("/Users/tc/Premier_League_Prediction/data/total.csv")

