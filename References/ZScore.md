Z-Score

What is Z-Score?

A Z-score is a numerical measurement used in statistics of a value's relationship to the mean (average) of a group of values, measured in terms of standard deviations from the mean. If a Z-score is 0, it indicates that the data point's score is identical to the mean score. A Z-score of 1.0 would indicate a value that is one standard deviation from the mean. Z-scores may be positive or negative, with a positive value indicating the score is above the mean and a negative score indicating it is below the mean.

The below formula explains each element utilized.

z = (x – μ) / σ
where:
x means each row in the list
μ = mean.
σ = the number of items in the group.

Utilization of Z-Score in our Code:

Zscore(val):
    m = mean(val)
    z = stddev(val)
    length = len(val)
    score = []
    for p in range(0, length, 1):
        zsc = 0
        zsc = round(float(division(z, sub(m, val[p]))), 3)
        score.append(zsc)
    return score
