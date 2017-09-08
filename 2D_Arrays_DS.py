#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
    
#Code starts here

arr_sum = [] ## 2-D - 4 x 4 array to store the sum of 16 hour glasses

#Append four 1_D array of length 4 containing zeros to the 4 X 4 array
for i in range(0,4,1):
    arr_sum.append([0,0,0,0])

#The maximum negative summation of 7 9's is -63. So we keep max as -64

max = -64
temp = 0 ##Temporary variable to store the value of an hour-glass while computing maximum element

## arr_temp = [] --- Test Array to check the values of temp variable

## Loop to store sum of hour glasses
## The positionn in summation_array i.e. arr_sum[i][j] gives the starting point Top-Left for Hour glass w.r.t input 6 x 6 
## input array arr 

for i in range(0,4,1):
    for j in range(0,4,1):
     #SUM of hour glass= top-left + top-middle + top-left    + middle-middle + bottom-left + bottom-middle + bottom-right
        arr_sum[i][j] = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        
## Loop to print the maximum element in 4 x 4 array

for i in range(0,4,1):
    for j in range(0,4,1):
        temp = arr_sum[i][j]
        ##arr_temp.append(temp)
        if temp >= max :
            max = temp
            
print(max)
