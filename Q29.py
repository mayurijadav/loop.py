a=[4,6,3,5,6,7,9,2]
i=0
b=[]
# c=[]
while i<len(a):
    if a[i]%2==0:
        b.append(0)
    else:
        b.append(a[i])
    i+=1
print(b)
 
