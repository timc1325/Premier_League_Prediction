import pandas as pd
def convert_outcome(url) -> pd.Series:
    a = pd.read_html(url)[2].drop([1,3,5,7],axis=0).fillna(0).reset_index(drop=True)

    home_possession = int(a.iloc[0,:][0].strip("%"))/100

    #extract str with # pass and # success rate given that all pass in game cannot go above 1000
    home_pass = int(a.iloc[1,:][0].split()[0])
    home_pass_success_rate = float(a.iloc[1,:][0].split()[-1].strip("%"))/100
    away_pass = int(a.iloc[1,:][1].split()[-1])
    away_pass_success_rate = float(a.iloc[1,:][1].split()[0].strip("%"))/100

    home_shot = int(a.iloc[2,:][0].split()[0])
    home_shot_on_target_rate = float(a.iloc[2,:][0].split()[-1].strip("%"))/100
    away_shot = int(a.iloc[2,:][1].split()[-1])
    away_shot_on_target_rate = float(a.iloc[2,:][1].split()[0].strip("%"))/100

    home_save = int(a.iloc[3,:][0].split()[0])
    home_save_success_rate = float(a.iloc[3,:][0].split()[-1].strip("%"))/100
    away_save = int(a.iloc[3,:][1].split()[-1])
    away_save_success_rate = float(a.iloc[3,:][1].split()[0].strip("%"))/100

    home_cards= int(a.iloc[4,:][0])
    away_cards= int(a.iloc[4,:][1])
    final_outcome= pd.DataFrame([home_possession,home_pass,home_pass_success_rate,
    away_pass,away_pass_success_rate,
    home_shot,home_shot_on_target_rate,
    away_shot,away_shot_on_target_rate,
    home_save,home_save_success_rate,
    away_save,away_save_success_rate,
    home_cards,away_cards])
    final_outcome.set_index(pd.Series(["home_possession","home_pass","home_pass_success_rate",
    "away_pass","away_pass_success_rate",
    "home_shot","home_shot_on_target_rate",
    "away_shot","away_shot_on_target_rate",
    "home_save","home_save_success_rate",
    "away_save","away_save_success_rate",
    "home_cards","away_cards"]),inplace=True)
    return final_outcome

