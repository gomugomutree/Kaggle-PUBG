import pandas as pd
from sklearn.preprocessing import StandardScaler
import src.feature as ft
import src.drop as dr


def scaling(data):
    scaler = StandardScaler()

    if type(data) == pd.DataFrame:
        new_data = scaler.fit_transform(data.values)
    else:
        new_data = scaler.fit_transform(data)

    return new_data


def preprocessing(df):
    if type(df) == pd.DataFrame:
        dr.drop_isna_game(df)
        dr.drop_event_game(df)

        ft.add_hackuser_include_game(df)
        dr.drop_hackuser_include_game(df)

        ft.add_match_type_numerical(df)
        ft.add_maptype(df) 

        ft.add_team_member_count(df)
        ft.select_teamdata_type(df)

        dr.final_drop_feature(df)
    else:
        return print('please input type : DataFrame')
    return df

