n = int(input())
k = int(input())

if k%n != 0:
    print(n - k%n)
else:
    print(0)