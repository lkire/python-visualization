import pandas as pd
import numpy as np

def toDataFrame(sklearnDataSet):
    """Returns a pandas dataframe from a sklearn dataset"""
    return pd.DataFrame(data = np.c_[sklearnDataSet['data'], sklearnDataSet['target']],
                        columns = list(sklearnDataSet['feature_names']) + ['target'])
