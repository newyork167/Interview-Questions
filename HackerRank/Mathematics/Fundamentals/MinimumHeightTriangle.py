#!/bin/python

# This challenge can be found at: https://www.hackerrank.com/challenges/lowest-triangle

# Basically you just want to take the normal formula of A = (1/2)B*H
# and rearrange it into 2*A/B = H
# This allows us to determine the smallest triangle of area at leastA and base B by
# finding the nearest minimum integer (the ceiling function) of this formula

import sys
import math

def lowestTriangle(base, area):
    return int(math.ceil(2.0*area/base))

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
