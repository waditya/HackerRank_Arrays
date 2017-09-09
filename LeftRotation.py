#!/bin/python3

import sys

##Code starts

def leftRotation(a, d):
    # Complete this function
    length = len(a)
    half_length = length / 2
    #print(length)
    if length == d:
        dummy = 0
    elif d <= half_length:
        for ctr in range(0, d, 1):
            a.append(a[ctr])                  
        del a[:d]
    else:
        for ctr1 in range(0, d, 1):
            a.append(a[ctr1])
        del a[:d]
    return(a)
    
##Code ends       

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))


