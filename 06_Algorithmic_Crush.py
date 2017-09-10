#!/bin/python3

import sys


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for ctr in range(n):
        arr.append(0)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        a = a - 1    
        
        for ctr1 in range(a, b, 1):
            arr[ctr1] = arr[ctr1] + k
            
    ## Print the maximum number in the array
    print(max(arr))
        
