## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q9: create a calss method to find a time and space complexity of any function

import time 
from mumpy import numpy as np


start = time.time()
total = 0
# finding sum of 1 to 1.5m .. iterating through 1.5 Million numbers
for item in range(0, 1500000):
    total = total + item
print('sum is:' + str(total))
end = time.time()

timetaken = end - start
print(f"Time taken {timetaken} for loop")

start = time.time()
print(np.sum(np.arange(1500000)))
end = time.time()

timetaken = end - start
print(f"Time taken {timetaken} with vectorization")


