def human_classify_move(power, accuracy):

    if power < 50:
        power_class = "Weak"
    elif power < 100:
        power_class = "Moderate"
    else:
        power_class = "Strong"

    if accuracy < 60:
        accuracy_class = "Low Accuracy"
    elif accuracy < 90:
        accuracy_class = "Moderate Accuracy"
    else:
        accuracy_class = "High Accuracy"
    
    return f"{power_class} & {accuracy_class}"