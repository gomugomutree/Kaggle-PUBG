#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_info_row', 100)
pd.set_option('display.max_info_columns', 100)


#%%
def read_train_file():
    data_path = 'C:/Users/hojun/Documents/dev/mini_project/data/train_V2.csv'
    data = pd.read_csv(data_path)
    return data

df = read_train_file()

#%%
print(df.info())
# print(df.describe())
print(df.describe(include='all'))
