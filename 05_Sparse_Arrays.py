#!/bin/python3

import sys

#!/bin/python3

import sys

arr_temp = input().strip().split(' ')
no_of_strings = int(arr_temp[0])
print(no_of_strings)

##Flush the temporary array

del arr_temp

## Read the next N ('no_of_strings') from input and store it in an array

arr_strings = []
for ctr in range(no_of_strings):
    arr_t = input().strip().split(' ')
    arr_strings.append(arr_t[0])
    del arr_t

## Display the array of strings(arrray to be searched from)
print(arr_strings)
      
##Accept the number of keywords to be searched in number_of_keywords

arr_temp = input().strip().split(' ')
number_of_keywords = int(arr_temp[0])



## Flush the temporary array

del arr_temp

## Print the number_of_keywords

print(number_of_keywords)

## Accept the strings to be searched in arr_search array
arr_search = []

for ctr1 in range(number_of_keywords):
    arr_t = input().strip().split(' ')
    arr_search.append(arr_t[0])
    del arr_t

## Display the search array arr_search
print(arr_search)




