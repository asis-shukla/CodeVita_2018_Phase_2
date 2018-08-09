"""This is a program for Obstacle problem
which is asked in TCS CodeVita phase 2 2018
This is written by Ashish Shukla on  10-08-2018"""

n = int(input())

arr = map(int, input().split())

arr_list = list(arr)
total = sum(arr_list)
arr_list.sort()


for k in range(n-1, -1, -1):
    rem_sum = total-arr_list[k]
    if rem_sum > arr_list[k]:
        print(k+1, end="")
        break
    total = total - arr_list[k]
else:
    print(0, end="")
