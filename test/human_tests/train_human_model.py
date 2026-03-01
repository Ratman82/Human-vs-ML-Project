import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from test.human_tests.human_classifier import human_classify
from test.data.fetch_data import load_moves
from sklearn.model_selection import train_test_split

df, target_name = load_moves()
df = df.dropna(subset=[target_name])

df['target_category'] = df.apply(human_classify, axis=1)

train_df, test_df = train_test_split(
    df,
    test_size=0.3,
    random_state=42,
    stratify=df['target_category']
)
print(df)

test_df['human_prediction'] = test_df.apply(human_classify, axis=1)
test_df['correct'] = test_df['human_prediction'] == test_df[target_name]
accuracy = (test_df['human_prediction'] == test_df[target_name]).mean()
print(f"Human classifier accuracy: {accuracy:.2%}")



failure_row = test_df[test_df['human_prediction'] != test_df['target_category']].iloc[0]
print("\nFAILURE EXAMPLE")
print(failure_row[['pp', 'power', 'target_category', 'human_prediction']])
os.makedirs("example/e_ml_model/plots", exist_ok=True)
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=test_df,
    x='power',
    y='pp',
    hue='correct',
    style='correct',
    s=100,
    palette={True: 'green', False: 'red'}
)
plt.title('Human Algorithm: Correct vs Incorrect Predictions')
plt.xlabel('Power')
plt.ylabel('PP')
plt.legend(title='Prediction Correct')
plt.grid(True)
plt.savefig('test/human_tests/plots/human_model_training_results.png', dpi=150)
plt.close()