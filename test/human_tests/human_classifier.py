def human_classify(power, pp):
    if power < 50 and pp > 20:
        return 'Iris-setosa'
    else:
        return 'Iris-virginica'