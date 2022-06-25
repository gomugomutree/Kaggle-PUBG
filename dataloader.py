import pandas as pd


base_path = ''

def load_data(data_type):
    # data_type : { 'train', 'test', 'submission' }

    if data_type == 'train':
        data = pd.read_csv(base_path + 'trian.csv')

    elif data_type == 'test':
        data = pd.read_csv(base_path + 'test.csv')

    elif data_type == 'submission':
        data = pd.read_csv(base_path + 'sample_submission_V2.csv')
