Sample Mean

What is Sample Mean?

Sample Mean is when we take a random sample from the entire population and calculate the mean for the randomly selected sample.

Calculating the Sample Mean:

ample_mean(val):
    ms = random.randint(1, len(val))
    val_new = sample(val, ms)
    p = round(mean(val_new), 2)
    true_mean = round(statistics.mean(val_new), 2)
    return p, true_mean
