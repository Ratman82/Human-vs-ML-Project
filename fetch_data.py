import pandas as pd
import seaborn as sns
import matplotlib as plt
import os

def load_moves():
    print('hello')
    file_path = './data/metadata_pokemon_moves.csv'

    df = pd.read_csv(file_path)
    print(df.head())

    target_name = "damage_class"
    X = df['id']
    y = df[target_name]
    return df, target_name


load_moves()