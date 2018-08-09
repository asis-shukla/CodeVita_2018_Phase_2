"""This is a program for Obstacle problem
which is asked in TCS CodeVita phase 2 2018
This is written by Ashish Shukla on 10-08-2018"""

import sys
sys.setrecursionlimit(1000)


def fun(x):
    if x == -1:
        return 0
    else:
        print("DESTINATION", end="")


def f(n, a, b, c):
    if b == -1:
        return
    else:
        pass
    x = -1
    y = -1
    u = -1
    v = -1
    l = 0
    s = 0
    t = 0
    w = 0
    for i in range(b-1, b+2):
        if 0 <= i < n:
            for j in range(c - 1, c + 2):
                if 0 <= j < n:
                    if a[i][j] == 'X' or a[i][j] == 'A' or a[i][j] == 'M':
                        pass
                    elif a[i][j] == 'R':
                        if (i == b) and (j == c):
                            a[i][j] = 'X'
                        else:
                            u, v = i, j
                    elif a[i][j] == 'D':
                            x, y = i, j

                    else:
                        if a[i][j] == 'L':
                            l+=1
                        elif a[i][j] == 'S':
                            s+=1
                        elif a[i][j] == 'T':
                            t+=1
                        elif a[i][j] == 'W':
                            w+=1
    for i in range(0, l):
        if i == l-1:
            print("L", end=" ")
        else:
            print("L", end=" ")

    for i in range(0, s):
        if i == s-1:
            print("S", end=" ")
        else:
            print("S", end=" ")
    for i in range(0, t):
        if i == t-1:
            print("T", end=" ")
        else:
            print("T", end=" ")
    for i in range(0, w):
        if i == w-1:
            print("W", end=" ")
        else:
            print("W", end=" ")
    print("\b", end="")
    print("\n", end="")
    fun(x)
    f(n, a, u, v)


i = 0
n = int(input())
a = []

for _ in range(n):
    temp_list = list(input().split(" "))
    a.append(temp_list)


if a[0][1] == 'R':
    f(n, a, 0, 1)
elif a[1][0] == 'R':
    f(n, a, 1, 0)
elif a[1][1] == 'R':
    f(n, a, 1, 1)

