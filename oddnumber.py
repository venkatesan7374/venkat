x=input().split()
a=int(x[0])
r=int(x[1])
for i in range(a+1,r):
    if(i%2!=0):
        print(i,end=' ')
