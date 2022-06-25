import json
import random
from src.feature import add_match_type_numerical
import pandas as pd

def load_config(model_name):
    with open(f'./config/{model_name}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def sampled_match_id(df):
    # df의 경기 id를 중복 제거 list로 만든다. 
    sample_matchId =list(set(df.matchId))

    # 임의로 섞어준다.
    random.shuffle(sample_matchId)
    
    # 1/5만 뽑아낸다.
    sample_matchId = sample_matchId[:int(len(sample_matchId)/5)]
    
    # list 반환
    return str(sample_matchId)



# match type(solo, duo, squad)별로 샘플링 해서 합쳐준다. 
def sampled_data(df):
    # match type 별 feature 생성
    df = add_match_type_numerical(df)
    
    # type별로 dataframe 나눈다.
    solo_df = df[df.match_type_numerical==0]
    duo_df = df[df.match_type_numerical==1]
    squad_df = df[df.match_type_numerical==2]

    # solo 경기 match id list 받기
    match_id = sampled_match_id(solo_df)

    # 샘플 추출
    sample_solo = solo_df[solo_df.matchId.apply(lambda x : True if match_id.find(x) != -1 else False)]

    # dou, squad 반복
    match_id = sampled_match_id(duo_df)
    sample_duo = duo_df[duo_df.matchId.apply(lambda x : True if match_id.find(x) != -1 else False)]
    
    match_id = sampled_match_id(squad_df)
    sample_squad = squad_df[squad_df.matchId.apply(lambda x : True if match_id.find(x) != -1 else False)]

    # 샘플데이터를 합쳐준다.
    sample_data = pd.concat([sample_solo, sample_duo, sample_squad])

    # 생성했던 feature를 제거
    sample_data = sample_data.drop(columns='match_type_numerical')
    
    return sample_data