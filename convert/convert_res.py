import pandas as pd
def convert_outcome(a: pd.DataFrame) -> pd.Series:
    x = a.drop([1,3,5,7],axis=0).fillna(0).reset_index(drop=True)
    
    def split_result_percentage(q:pd.DataFrame, option, order): 
        if order ==0:
            c,p= 2,-1
        else:
            c,p= -1,0
        result = int(q.iloc[option,:][order].split()[c])
        temp =  q.iloc[option,:][order].split()[p].strip("%")
        percentage=  float(temp if temp!="" else 0)/100
        return result,percentage
    #extract str with # pass and # success rate given that all pass in game cannot go above 1000

    home_possession = int(x.iloc[0,:][0].strip("%"))/100

    home_pass,home_pass_success_rate = split_result_percentage(x,1,0)
    away_pass,away_pass_success_rate = split_result_percentage(x,1,1)
    home_shot,home_shot_on_target_rate = split_result_percentage(x,2,0)
    away_shot,away_shot_on_target_rate = split_result_percentage(x,2,1)
    home_save,home_save_success_rate = split_result_percentage(x,3,0)
    away_save,away_save_success_rate = split_result_percentage(x,3,1)

    home_cards= int(x.iloc[4,:][0])
    away_cards= int(x.iloc[4,:][1])
    final_outcome= pd.DataFrame([home_possession,
                                home_pass,home_pass_success_rate,
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

