#!/bin/python

# Challenge can be found here: https://www.hackerrank.com/challenges/game-with-cells

# We want to find the minimum number of drops to fully supply all army bases
# So if we take a look at a random set of grids we can come up with the following algorithm
# The number of rows / 2 since each drop will be able to handle 2 drops for each row
# We also know that the same holds for columns
# So we just need to multiply these values together to get the minimum number of drops

import sys
import math

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

print(int(math.ceil(n/2.0)*math.ceil(m/2.0)))