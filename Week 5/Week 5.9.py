a=input()
i=0
x=''
y=''
z=''
while(i<len(a)):
    if(a[i]=='@'):
        break
    else:
        x+=a[i]
    i+=1
i+=1
while(i<len(a)):
    if(a[i]=='.'):
        break
    else:
        y+=a[i]
    i+=1
i+=1
while(i<len(a)):
    z+=a[i]
    i+=1
print(z)
print(y)
print(x)