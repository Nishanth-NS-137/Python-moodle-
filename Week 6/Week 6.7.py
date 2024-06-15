test=int(input())
while(test!=0):
    n=int(input())
    list=[]
    for i in range(0,n):
        a=int(input())
        list.append(a)
    k=int(input())
    flag=0
    for i in range(0,n):
        for j in range(0,n):
            if i!=j:
                if flag==0:
                   if list[i]-list[j]==k or list[i]-list[j]==-k:
                      print("1")
                      flag=1
                      break
    if flag==0:
        print("0")
    test=test-1
