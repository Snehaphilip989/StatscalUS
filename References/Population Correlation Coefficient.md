# What is Correlation Coefficient?

The correlation coefficient is a statistical measure that calculates the strength of the relationship between the relative movements of 
two variables. The values range between -1.0 and 1.0. A calculated number greater than 1.0 or less than -1.0 means that there was an error in the correlation measurement. A correlation of -1.0 shows a perfect negative correlation, while a correlation of 1.0 shows a perfect positive correlation. A correlation of 0.0 shows no relationship between the movement of the two variables.

1 indicates a strong positive relationship.
-1 indicates a strong negative relationship.
A result of zero indicates no relationship at all.

Utilization of Correlation Coefficient in our Code:

pop_corr_coef(val, val1):
    x1 = Zscore(val)
    x2 = Zscore(val1)
    x1_x2 = list(map(lambda x, y: x * y, x1, x2))
    y = sum(x1_x2) / len(x1_x2)
    return y
    
    
