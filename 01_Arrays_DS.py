#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

#! Code starts here

#Reverse the order of display and use " " as the value for argument 'end' of print function

for i in range(n-1,-1,-1):
    print(arr[i], end = " ")
