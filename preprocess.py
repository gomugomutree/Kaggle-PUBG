import pandas as pd
from sklearn.preprocessing import StandardScaler
import src.feature


def scaling(data):
    scaler = StandardScaler()

    if type(data) == pd.DataFrame:
        new_data = scaler.fit_transform(data.values)
    else:
        new_data = scaler.fit_transform(data)

    return new_data



def preprocessing(test_data):
    test_data['match_type_numerical'] = test_data['matchType'].apply(lambda x : src.feature.divide_match_type(x) )

    # add maptype
    test_data['maptype'] = test_data['matchDuration'].apply(lambda x : 0 if x<1600 else 1)

    # add team members
    test_data['team_members'] = test_data.groupby('groupId').Id.transform('count')

    # drop colums
    drop_columns = ['killStreaks','headshotKills', 'assists', 'matchDuration','matchType', 'swimDistance', 'vehicleDestroys', 'roadKills', 'DBNOs', 'revives', 'teamKills','killPoints', 'winPoints', 'rankPoints', 'numGroups' ]
    test_data = test_data.drop(columns=drop_columns).copy()
    return test_data

