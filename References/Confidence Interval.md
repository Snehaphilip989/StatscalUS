                                                  Confidence Interval

What is the Confidence Interval?
In statistics, a confidence interval (CI) or the confidence level represents the frequency (i.e. the proportion) of possible confidence intervals that contain the true value of the unknown population parameter.

Confidence intervals consist of a range of potential values of the unknown population parameter. However, the interval computed from a particular sample does not necessarily include the true value of the parameter. Based on the (usually taken) assumption that observed data are random samples from a true population, the confidence interval obtained from the data is also random.

Calculating the Confidence Interval:

The formula to calulate the Confidence Interval is given by:

CI = X  ±  Z * s/√n
Confidence Interval gives us a range by giving an upper limit and a lower limit Here, xi , yi are the elements in 2 lists

    X is the mean of the sample
    
    s is the standard deviation of the sample
    
    n is the number of elements in the sample (sample size)
    
    Z value is based on the confidence interval percentage
Z value varies based on the confidence percentage as follows:

Confidence Interval	Z
80%	1.282
85%	1.440
90%	1.645
95%	1.960
99%	2.576
99.5%	2.807
99.9%	3.291

Utilization of Confidence Interval in our Code

In order to calculate the Confidence Interval, we have assumed the confidence level to be 95 %. This gives us a z value of 1.960 by taking alpha as 5% (0.05). Now we calculate the mean and the standard deviation of the population taken from the StatCalcData.csv file and calculate the upper and lower limits of the confidence interval accordingly.
