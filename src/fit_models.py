RANDOM_SEED = 42
import numpy as np
np.random.seed(RANDOM_SEED)

import random
random.seed(RANDOM_SEED)

import config as cfg
from utils import get_repo_path
import pandas as pd
import json
import dvc.api

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


METRICS_FILE = 'eval/metrics.json'

models = {
    'rf': RandomForestClassifier(),
    'cart': DecisionTreeClassifier(),
    'svm': SVC(),
    'knn-2': KNeighborsClassifier(n_neighbors=2),
    'knn-3': KNeighborsClassifier(n_neighbors=3),
    'knn-5': KNeighborsClassifier(n_neighbors=5),
    'knn-7': KNeighborsClassifier(n_neighbors=7)
}


def prepare_data(df: pd.DataFrame) -> (pd.DataFrame, pd.Series):

    # Shuffle the data
    df = df.sample(frac=1)

    X = df[cfg.COLUMN_NAMES]
    y = df[cfg.TARGET]

    return X, y


def evaluate_model(model_name: str,
                   X: pd.DataFrame,
                   y: pd.Series) -> float:

    model = models[model_name]
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

    return scores.mean()


def main():
    # Read data
    df = pd.read_csv(get_repo_path() / cfg.DATA_PATH / cfg.INPUT_FILE)

    # Read parameters
    params = dvc.api.params_show()
    model_name = params['evaluate']['model']

    X, y = prepare_data(df)

    score = evaluate_model(model_name, X, y)

    with open(get_repo_path() / METRICS_FILE, 'w') as f:
        json.dump({'avg_accuracy': score}, f)


if __name__ == '__main__':
    main()













