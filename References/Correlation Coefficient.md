Population Correlation Coefficient

What is Population Correlation Coefficient?

Population Correlation coefficients measure the strength of association between two variables or a set of variables.There are different methods for calcualting the correlation coefficient. The most common method of finding the correlation coefficient is called the Pearson product-moment correlation coefficient. It measures the strength of the linear association between variables measured on an interval or ratio scale.

Calculating the Correlation Coefficient:
The formula to calulate the Correlation Coefficient is given by:

    x1 = Zscore(val)
    x2 = Zscore(val1)
    x1_x2 = list(map(lambda x, y: x * y, x1, x2))
    y = sum(x1_x2) / len(x1_x2)
    return y
    
   
Utilization of Correlation Coefficient in our Code : To calculate the variables as how much are they correlated. The values ranges between -1 to +1. 
Correaltion value from 0.4 and above is found to be strongly correlation. And value between 0.2 and 0.4 is moderatelt correlated and below 0.2 is considered as weak coreelation. 
