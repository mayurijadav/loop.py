a=[2,3,4,5,6,7,8,9,23,34,45]
i=0
count=0
while i<len(a):
    if a[i]%2==0:
        count=count+1
    i+=1
print(count)
    