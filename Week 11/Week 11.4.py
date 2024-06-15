import math
try :
    n=float(input())
    m=n**0.5
    if 0<=n:
        print(f"The square root of {n} is {m:.2f}")
    else:
        print("Error: Cannot calculate the square root of a negative number.")
except:
    print("Error: could not convert string to float")
