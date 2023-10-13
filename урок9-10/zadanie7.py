a = str(input())

if len(a[::-1]) <= 2:
    print(False)
elif a[::-1][2] > a[::-1][1]:
    print(True)
else:
    print(False)