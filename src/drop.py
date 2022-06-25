

# isna : True -> game drop
def drop_isna_game(df):
    df = df.drop(index=df[df.matchId == df[df['winPlacePerc'].isna()].matchId].index).copy()
    return df

# Event game Drop
def drop_event_game(df):
    drop_event = ['crashfpp', 'flaretpp', 'flarefpp', 'crashtpp']
    for i in drop_event:
        index_names = df[df['matchType'].str.contains(i)].index
        df = df.drop(index_names).copy()
    return df


# Unused feature drop
def final_drop_feature(df):
    # drop colums
    drop_columns = ['groupId', 'matchId', 'killStreaks','headshotKills', 'assists', 'matchDuration','matchType', 'swimDistance', 'vehicleDestroys', 'roadKills', 'DBNOs', 'revives', 'teamKills','killPoints', 'winPoints', 'rankPoints', 'numGroups','killPlace', 'team_members' ]
    df = df.drop(columns=drop_columns).copy()
    return df


# 핵유저 포함 경기 제외 
def drop_hackuser_include_game(df):
    df = df[df.hack_user_game == 0]
    df = df.drop(columns='hack_user_game').copy()
    return df