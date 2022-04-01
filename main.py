# Daily Code

import random

# 1. Given a list of numbers and a number k, return whether any two numbers in the list add up to k.
# For example, given a list [12, 4, 19, 8], and a k of 16, return true, that 12 +  4 = 16.

k = 10

list = [12, 33, 45, 88, 100, 2, 1, 3, 4, 6]

def sum_numbers(list,k):
    for i in range(len(list)):    # range(len(list)) == from start to finish of the length of the list
        for j in range(len(list)):
            if i != j and list[i] + list[j] == k:  # list[i] == list at element i
                print("True")
                print(list[i], list[j])

sum_numbers(list,k)





