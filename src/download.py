from sklearn import datasets
import pandas as pd
from utils import get_repo_path
import config as cfg


def main():
    iris = datasets.load_iris()

    # Create dataframe
    df = pd.DataFrame(iris['data'])
    df.columns = cfg.COLUMN_NAMES

    # Add column with species' names
    df[cfg.TARGET] = iris['target']
    target_names = {index: name for index, name in enumerate(iris['target_names'])}
    df[cfg.TARGET] = df[cfg.TARGET].replace(target_names)

    df.to_csv(get_repo_path() / cfg.DATA_PATH / cfg.INPUT_FILE, index=False)


if __name__ == '__main__':
    main()
