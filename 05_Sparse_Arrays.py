#!/bin/python3

import sys

arr_temp = input().strip().split(' ')
no_of_strings = int(arr_temp[0])

## print(no_of_strings) ## [--DEBUG--01]

##Flush the temporary array

del arr_temp

## Read the next N ('no_of_strings') from input and store it in an array

arr_strings = []
for ctr in range(no_of_strings):
    arr_t = input().strip().split(' ')
    arr_strings.append(arr_t[0])
    del arr_t

## Display the array of strings(arrray to be searched from)
## print(arr_strings) ## [--DEBUG--01]
      
##Accept the number of keywords to be searched in number_of_keywords

arr_temp = input().strip().split(' ')
number_of_keywords = int(arr_temp[0])



## Flush the temporary array

del arr_temp

## Print the number_of_keywords

## print(number_of_keywords) ## ## [--DEBUG--03]

## Accept the strings to be searched in arr_search array
arr_search = []

for ctr1 in range(number_of_keywords):
    arr_t = input().strip().split(' ')
    arr_search.append(arr_t[0])
    del arr_t

## Display the search array arr_search
## print(arr_search) ## [--DEBUG--04]

## Search the array terms in arr_search in array of strings arr_string

##Apply constraints while searching

if number_of_keywords <= 1000 and no_of_strings <=1000:
    arr_count = []
    ## arr_count = [0, 0, 0]  [--DEBUG -- :Hardcoded Array to debug custom input]
    for ctr_number_of_keywords in range(number_of_keywords):
        arr_count.append(0)
        
    ##Initialize the arr_count
    for ctr_search in range(number_of_keywords):
        for ctr_strings in range(no_of_strings):
            if arr_search[ctr_search]== arr_strings[ctr_strings]:
                arr_count[ctr_search] = arr_count[ctr_search] + 1
        print(arr_count[ctr_search])



