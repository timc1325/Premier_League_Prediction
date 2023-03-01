import pandas as pd
import datetime as dt
class Player():
  def __init__(self, name: str, stat:pd.DataFrame):
    self.name = name
    self.stat = stat #stat include date

class Team():
  def __init__(self, name: str, squad: list[Player], matches: pd.DataFrame):
    self.name = name
    self.squad = squad 
    self.matches = matches #matches include date 




