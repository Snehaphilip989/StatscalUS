# What is Mode?

A Mode is the most recurring number in a given list.

Utilization of Mode in our Code: 

The below logic would take the maximum count of a number in the list we used to capture the mode.

    for q in range(0, length, 1):
        modelst.append(numbers.count(numbers[q]))
    p = max(modelst)
    for x in numbers:
        if numbers.count(x) == p:
            return x
