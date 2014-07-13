Title: My super title
Date: 2014/05/27 10:20
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Author: Prateek Singhal
Summary: Short version for index and feeds

This is the content of my super blog post.

### Simple Linear Regression using Python Multiprocessing library

I recently learned executing "Simple Linear Regression" using `multiprocessing` module in python. This module is used for parallel processing in python. The `β` for Simple Linear Regression is calculated using the following formula:

![alt text](http://www.sciweavers.org/download/Tex2Img_1405242253.jpg "Logo Title Text 1")

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