                                                        Median

What is Median?

A Median is a middle number in a data set. It is a sorted list in ascending order.

For an odd list of numbers, there will always be a singular middle number. For an even list of numbers, there will be two values which can be further calculated by adding the two numbers and dividing by two to extract the median.

The below formula explains each element utilized:

Utilization of Median in our Code

We initially sorted out list of data
numbers.sort()

median(numbers):
    length = len(numbers)
    numbers.sort()
    if length % 2 == 0:
        med_1st = numbers[int(division(2, length))]
        med_2nd = numbers[len(numbers) // 2 - 1]
        mid = division(2, addition(med_1st, med_2nd))
    else:
        mid = numbers[division(2, length)]
    return mid
