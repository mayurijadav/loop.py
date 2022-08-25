a=[1,0,1,0,1,0,1,0,1]
i=0
sum=""
while i<len(a):
    sum=sum+str(a[i])
    i+=1
# print(sum)
n=int(sum)
i=0
sum=0
while n>0:
    sum+=(n%10*(2**i))
    n=n//10
    i+=1
print(sum)

# a=[1,0,0,1,1,0,1]
# i=0
# while i<len(a):
#     reverse=a[i]
# print(reverse)


    
