n = int(input())


f = [0] * (n+1)
def fibonacci(n):
    f[1] = f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


print(fibonacci(n), n-2)