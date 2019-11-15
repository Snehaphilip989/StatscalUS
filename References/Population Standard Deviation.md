# Population Standard Deviation

## What is Population Standard Deviation?

Standard deviation is a calculation of the dispersion or variation in a set of numbers. If the standard deviation is a small number, it means the data points are close to their mean value. If the deviation is large, it means the numbers are spread out, further from the mean.

## The standard deviation formula is denoted by the following:

σ = ([Σ(x - u)2]/N)1/2
Where:

σ is the population standard deviation
Σ represents the sum or total from 1 to N
x is an individual value
u is the average of the population
N is the total number of the population

Utilization of Population Standard Deviation in our Code:

Stddev(numbers):
    length = len(numbers)
    y = 0
    n = 0
    for p in range(0, length, 1):
        y = sub(mean(numbers), numbers[p])
        n = addition(square(y), n)
    x = division((length - 1), n)
    return sqroot(x)
    
   
