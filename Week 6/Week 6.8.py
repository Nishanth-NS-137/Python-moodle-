l1=[]
for i in range(10):
    a=int(input())
    l1.append(a)
n=int(input())
index_to_insert = 0
for i in range(10):
    if l1[i] > n:
        index_to_insert = i
        break
    index_to_insert = i + 1
l1.insert(index_to_insert,n)
print("ITEM to be inserted:",n,sep="")
print("After insertion array is:")
for num in l1:
    print(num)
