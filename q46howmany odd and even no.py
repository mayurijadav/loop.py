elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
e=[]
while i<len(elements):
    if elements[i] %2==0:
        e.append(elements[i])
        # count=count+elements[i]
        # count=count+elements[i]
    else:
        e.append("odd no")
        count=count+elements[i]
        # count=count+int(e)
    i+=1
print(e)


