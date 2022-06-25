from src.hackuser import hack_users

# add match_type_numerical
def divide_match_type(x):
    # game type : solo -> 0  duo -> 1  suad -> 2 
    # apply method 사용시 
    if x.find('solo') != -1:
        return 0
    elif x.find('duo') != -1:
        return 1
    else:
        return 2

# add match type numerical feature 
def add_match_type_numerical(df):
    df['match_type_numerical'] = df['matchType'].apply(lambda x : divide_match_type(x) )
    return df

# add map type feature 
def add_maptype(df):
    # 1600을 기점으로 두 map으로 나누어 진다.
    # small map -> 0   large map _> 1
    df['maptype'] = df['matchDuration'].apply(lambda x : 0 if x<1600 else 1)
    return df

# add team member count feature 
def add_team_member_count(df):
    df['team_members'] = df.groupby('groupId').Id.transform('count')
    return df

# add hack user include game feature
def add_hackuser_include_game(df):
    # 핵 유저만 따로 찾는다.
    hack_user = hack_users(df)

    # 핵 중복 사용 유저 정리
    hack_user = hack_user.drop_duplicates('Id') 

    # 핵 유저 경기 id를 string 형태로 만든다.
    hack_user_matchid = str(list(hack_user.matchId.values))

    # 핵 유저가 참가한 경기 -> 1  참가 안한 경기 -> 0
    df["hack_user_game"] = df.matchId.apply(lambda x : 0 if hack_user_matchid.find(x)==-1 else 1) # find 함수는 찾지 못하면 -1 반환
    
    return df
