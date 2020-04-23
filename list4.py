a=[2,3,4,9,0]
b=[]
a.sort()
while(a[0]<a[1]):
    b=a[1]
    a[1]=a[0]
    a[0]=b
print(a)
