import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def fill_missing_median(df, columns):
    df = df.copy()

    for col in columns:
        df[col] = df[col].fillna(df[col].median())

    return df


def drop_missing(df, threshold=0.5):
    df = df.copy()

    # Keep rows whose missing proportion is below threshold
    df = df[df.isna().mean(axis=1) < threshold]

    return df


def normalize_data(df, columns):
    df = df.copy()

    scaler = MinMaxScaler()

    df[columns] = scaler.fit_transform(df[columns])

    return df