#Python Program to Calculate Mean, Median, Mode and Standard Deviation
#By Bishworaj Poudel for students

import numpy as np
from scipy import stats

value = [21, 50, 62, 85, 90]

mean = np.mean(value)
median = np.median(value)
mode = stats.mode(value)
sd = np.std(value)

print(f"Mean is {mean}")
print(f"Median is {median}")
print(f"Mode is {mode}")
print(f"SD is {sd}")
