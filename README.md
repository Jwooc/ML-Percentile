# Percentile

Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

A percentile is a term used to describe and interpret data distributions.

The nth percentile describe the percentage of data below that percentile.

- For example, if in a class of 20 students, we find that the 25th percentile age is 20 years, it means that 25% of the students (in this case, 5 students) are below 20 years.

_n = (P / 100) * N_

where _P_ is _the percentile_, _N_ is _the number of data points_ in that dataset, and _n_ is _the number of data points_.

- For example, we have 10 marks in an exam, [50, 30, 20, 60, 73, 88, 44, 22, 67, 10], in order to obtain the _50_ th _percentile_:
    - Obtain _n_ using the formula, _50/100*10=5_. This means that the _50_ th _percentile_ is located in the _5_ th position in that dataset.
    - Order the dataset from the smallest to the largest. [10, 20, 22, 30, 44, 50, 60, 67, 73, 88], the _5_ th number is _44_. This means that _50_% of the students scored below _44_ marks.

`Note:` _The median_ is also known as _the 50th percentile_


    import numpy as np
    data = [50,30,20,60.73,88,44,22,67,10]
    perc = np.percentile(data, 50)
    print("50th percentile is", perc)
