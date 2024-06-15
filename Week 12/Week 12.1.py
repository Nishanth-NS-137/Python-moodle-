n=int(input())
if n<=0:
    print(False)
else:
    while n % 3 == 0:
        n//=3
    print(n == 1)
