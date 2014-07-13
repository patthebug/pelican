Title: My super title
Date: 2014/05/27 10:20
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Author: Prateek Singhal
Summary: Short version for index and feeds

### Simple Linear Regression using Python Multiprocessing library

I recently learned executing "Simple Linear Regression" using `multiprocessing` module in python. This module is used for parallel processing in python. The `β` for Simple Linear Regression is calculated using the following formula:

$\beta  = \frac {\sum_{i=1}^{n} x_{i}y_{i} -  \frac {1}{n} \sum_{i=1}^{n} x_{i} \sum_{j=1}^{n} y_{j}} {\sum_{i=1}^{n} x_{i}^{2} - \frac {1}{n}(\sum_{i=1}^{n} x_{i})^2}$

We will use the `multiprocessing` and `numpy` modules for this task.

```
import numpy as np
import multiprocessing as mp
```

The dataset that I will be using for this task is freely downloadable from [here](ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/nhanes/nhanes3/1A/adult.dat).  

I will regress `age` against `weight`. The following function may be used to read the file in:

```
def map_func(f):
    age = int(f[17:19]) #18-19
    wtlbs = int(f[1950:1953]) #1951-1953 wt in lbs, self reported !888! !999!
    return [age, wtlbs]
```