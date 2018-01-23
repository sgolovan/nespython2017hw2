def sumThreeFive(n):
    a = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            a += i
    return a


print(sumThreeFive(int(input())))
