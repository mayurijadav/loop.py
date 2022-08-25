
a=[2,48,42,3,73,8,9,6,8]
i=0
b=0
c=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>b:
            b=a[j]
            # print(b)
        elif a[j]>c  and a[j]!=b:  
            c=a[j]
         # print(c)    
        j=j+1
    i+=1
print(c)




# a=[23,45,6,34,23,67,87,65]
# i=0
# max=0
# max1=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     elif a[i>max1] and a[i]<max:
#         max1=max1<max
#     i+=1
# print(max)
# print(max1)

 


# # a=[12,34,55,26,23,28,12,54,56,76,12]
# a=[58,40,23,0,56,12,5,10,7,57,59]
# i=0
# max=0
# max2=0
# while i<len (a):
#     if a[i]>max:
#         max=a[i]
#         # i+=1
#         # print(max)
#     if a[i]>max2 and a[i]!=max :
#         max2=a[i]
#     i+=1
# print(max2)
