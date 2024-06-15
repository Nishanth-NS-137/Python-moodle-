s1=int(input())
s2=int(input())
s3=int(input())
if(s1==s2)&(s2==s3)&(s3==s1):
    print("That's a equilateral triangle")
elif(s1==s2)&(s1!=s3):
    print("That's a isosceles triangle")
else:
    print("That's a scalene triangle")
