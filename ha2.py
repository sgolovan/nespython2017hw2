#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sumThreeFive(n):
    sum = 0
    n = int(n)
    for x in range(0,n):
        if x%3 == 0 or x%5 == 0:
            sum = sum+x
        #print(sum, x)
    return sum

def fibo(n):
    n = int(n)
    if n==2:
        return 2
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)