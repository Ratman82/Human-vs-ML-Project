import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from test.data.fetch_data import load_moves

df, target_name = load_moves()

X = df[['power', 'pp']]
y = df[target_name]
X = X.dropna()
y = y[X.index]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
y_train_pred = knn.predict(X_train)

conf_matrix_knn = pd.crosstab(
    y_test,
    y_pred,
    rownames=['Actual'],
    colnames=['Predicted']
)

accuracy_knn = (y_pred == y_test).mean()

print(f"KNN classifier accuracy (k={k}): {accuracy_knn:.2%}\n")
print(conf_matrix_knn)

test_df = X_test.copy()
test_df[target_name] = y_test
test_df['KNN_prediction'] = y_pred
test_df['correct'] = test_df['KNN_prediction'] == test_df[target_name]

train_df = X_train.copy()
train_df[target_name] = y_train
train_df['KNN_prediction'] = y_train_pred
train_df['correct'] = train_df['KNN_prediction'] == train_df[target_name]

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

plt.title('KNN Algorithm: Correct vs Incorrect Predictions')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend(title='Prediction Correct')
plt.grid(True)
plt.savefig('test/ml_model/plots/knn_model_test_results.png', dpi=150)
plt.close()