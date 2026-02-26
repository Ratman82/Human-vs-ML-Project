import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from test.human_tests.human_classifier import human_classify
from test.data.fetch_data import load_iris_data
from sklearn.model_selection import train_test_split

df, target_name = load_moves()
train_df, test_df = train_test_split(
    df,
    test_size=0.3,
    random_state=42,
    stratify=df[target_name]
)

test_df['human_prediction'] = test_df['petal width'].apply(human_classify)
test_df['correct'] = test_df['human_prediction'] == test_df[target_name]
accuracy = (test_df['human_prediction'] == test_df[target_name]).mean()
print(f"Human classifier accuracy: {accuracy:.2%}")