import numpy as np

data = [50,30,20,60.73,88,44,22,67,10]

perc_test = np.percentile(data, 50)

print("50th percentile is", perc_test)
