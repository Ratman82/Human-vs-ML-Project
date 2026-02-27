def human_classify(power):
    if power < 0.6:
        return 'Iris-setosa'
    elif power < 1.6:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'