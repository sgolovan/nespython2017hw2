def fibo(n):
    def inFibo(a, b, c):
        if c == 1:
            return b
        return inFibo(a + b, a, c - 1)
    return inFibo(2, 1, n)


print(fibo(int(input())))
