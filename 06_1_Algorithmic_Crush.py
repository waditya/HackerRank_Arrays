#!/bin/python3
##[Credits] - https://www.hackerrank.com/vineet_ahirkar?hr_r=1 , https://www.hackerrank.com/challenges/crush/forum

## Accept the first line of the input
no_of_elememts_in_array, no_of_operations = [int(n) for n in input().split(" ")]

##print(no_of_elememts_in_array) ## -- DEBUG n = no_of_elememts_in_array
##print(no_of_operations) ## -- no_of_operations


list = [0]*(no_of_elememts_in_array+1)
##print(list) ## -- DEBUG - Check if all the elememts in the list are marked zero

## Read the operations using for loop for 'no_of_operations' times
for _ in range(no_of_operations):
    x, y, incr = [int(n) for n in input().split(" ")]
    ## Increment the element in lowerbound index
    list[x-1] += incr
    
    if((y)<=len(list)): 
        list[y] -= incr;
max = x = 0
for i in list:
    x=x+i;
    if(max<x): max=x;
print(max)
