from dataloader import load_data
from preprocess import scaling
from preprocess import preprocessing
from utils import load_config

from sklearn.ensemble import RandomForestClassifier


def main():
    # TODO python argparse package(library)
    # python main.py --config rf.json
    # python main.py --config svm.json
    # python main.py --config lr.json

    train_data = load_data(data_type='train')
    test_data = load_data(data_type='test')
    submission = load_data(data_type='submission')

    train_data = preprocessing(train_data)
    test_data = preprocessing(test_data)

    X = train_data.drop(columns='winPlacePerc')
    y = train_data.winPlacePerc


    cfg = load_config(model_name='rf')

    preprocess_cfg = cfg['preprocess']
    model_cfg = cfg['params']

    new_X = X
    if preprocess_cfg['scaling']:
        new_X = scaling(X)

    model = RandomForestClassifier(**model_cfg)
    model.fit(new_X, y)
    print("Done")
    # TODO evaluate


if __name__ == "__main__":
    main()