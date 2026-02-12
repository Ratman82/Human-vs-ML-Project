import pandas as pd
import seaborn as sns
import matplotlib as plt
import os

def load_moves():

    file_path = '/workspaces/Human-vs-ML-Project/data/metadata_pokemon_moves.csv'

    df = pd.read_csv(file_path)

    target_name = "damage_class"
    X = df['id']
    y = df[target_name]

    return df, target_name



    