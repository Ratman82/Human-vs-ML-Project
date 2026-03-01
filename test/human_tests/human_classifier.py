def human_classify(power, pp):
    if power < 50 and pp > 20:
        return 'Physical'
    else:
        return 'Special'