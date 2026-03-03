# Human vs Machine Learning Project

This project challenges you to explore the differences between human-designed algorithms and machine learning models. You will first create a human algorithm (pseudo-code) to classify data based on features, then translate that algorithm into Python. Next, you will train a K-Nearest Neighbors (KNN) classifier on the same dataset and compare your results. Finally, you will record a short screen-share with narration explaining your methods and observations.

You may work alone or with a partner. You may choose to work with the provided Penguins dataset, or select your own pre-cleaned dataset from the links below (I have suggested a few datasets as a guide, but you are welcome to select something different with approval).  The most important detail regarding your data-set is that your data needs to lend itself to classification.  For example, an iris with a sepal length of x and a petal width of y can be classified as ‘Setosa’. I also recommend that you use github codespaces, as you will need access to command-line tools that are unavailable in VS Code for EDU.

[UCI Machine Learning Repository](https://archive.ics.uci.edu/datasets)
 - Iris (classic 3-class classification)
 - Mushroom (binary classification: edible/poisonous)
 - Student Performance (predict grades, numeric features)

[Kaggle Datasets](https://www.kaggle.com/datasets)   *Note: For Kaggle, I will have to download the data for you and post on a shared drive.
 - Titanic survival dataset (binary classification)
 - Heart disease dataset (binary classification)
 - Breast cancer diagnosis (binary)
 - Penguins dataset (same as Kira, already cleaned)

---

**Team Members:**  
- Lukas  

**Dataset Used:**  
Pokemon Movesets

**Source:**  
(Kaggle)

**Target Variable (What I am predicting):**  
(Move power based on accuracy)

<img width="315" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/test/getting_started/plots/accuracy_v_power.png" />

<img width="315" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/test/getting_started/plots/power_v_pp.png" />

<img width="315" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/test/getting_started/plots/id_v_accuracy.png" />

**Features Used:**  
- Power
- PP
- Damage Class

**[Video Review](https://)**

## Human Algorithm

### Pseudo-Code
```text
If its before 50 power and above 20 pp its Physical else its special.

def human_classify(power, pp):
    if power < 50 and pp > 20:
        return 'Physical'
    else:
        return 'Special'

```

When examining the data and visualizations, I focused on the features power and pp because the data set used didn't seem to have the best graphs.

The plots/tables suggested a possible threshold for pp and power, and I considered values above or below this point to see how they might relate to Damage class.

From the summary tables and visualizations, it appeared that both pp and power could influence classification, which led me to both in decision rules.

### Confusion Matrix

Accuracy: 44.97%

Prediction:| Special | Actual:| Physical |
Prediction:| Special | Actual:| Physical |
Prediction:| Special | Actual:| Physical |
Prediction:| Special | Actual:| Physical |
Prediction:| Special | Actual:| Physical |
Prediction:| Special | Actual:| Physical |


For the human algorith it didnt really do well and got a less than 50% but it makes sense because the graph used it difficult to find a good pattern

An example where the algorithm did not perform as expected is when the inputs were to similar, resulting in a prediction of Special instead of Physical, which may have happened because there wasnt a clean method to sort them.

These examples of success and failure highlight patterns in the data or limitations in our rules, such as the limited data to use in graphing.

<img width="315" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/test/human_tests/plots/human_model_training_results.png" />

## Machine Learning Model

I chose a value of k = 4 after comparing model performance across different values of k and observing that it gave the best results.

When analyzing the outputs and metrics, I noticed that changing k affected accuracy in the model, which influenced our final choice.

Based on the results shown in the tables or visualizations, k = 4 best matched our goals for model performance because anything higher or lower gave worse results.

### Confusion Matrix

Accuracy: 65.75%

Predicted  Physical  Special
Actual                      
Physical         80        8
Special          42       16

The confusion matrix reveals that the model most often confuses Special with Pyhysical, suggesting these classes have similar feature values.

Compared to the human algorithm, the KNN model shows different behavior when K= 4, as seen in the KNN visualization.


KNN classifier accuracy (k=1): 55.48%

Predicted  Physical  Special
Actual                      
Physical         47       41
Special          24       34

Another reason why I bumped it up to 4 was because when I copied the code with the base K of 1 it had a lower accuracy compared to when I tried it with K of 4.

<img width="315" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/test/ml_model/plots/knn_model_test_results.png" />
Versus
<img width="315" height="334" alt="image" src="/workspaces/Human-vs-ML-Project/test/ml_model/plots/knn_model_test_results copy.png" />
