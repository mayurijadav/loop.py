a=[[23,45,57,56],[67,78,67,65,89],[67,67,85,96]]
i=0
sum=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i+=1
print(sum)


# a=[[23,45,57,56],[67,78,67,65,89],[67,67,85,96]]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]%2==0:
#             b.append(a[i][j])
#         elif a[i][j]%2!=0:
#             c.append(a[i][j])
#         j+=1
#     i+=1
# print(b)
# print(c)

# a=[[23,45,57,56],[67,78,67,65,89],[67,67,85,96]]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]%2==0:
#             b.append (a[i][j])
#         else:
#             c.append (a[i][j])
#         j+=1
#     i+=1
# print(b)
# print(c)
            