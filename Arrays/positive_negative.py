arr = [1, -2, 4, -5, 6]
pos=[]
neg=[]
for i in range (len(arr)):
    if arr[i] > 0 :
        pos.append(arr[i])
    else :
        neg.append(arr[i])
print(pos)
print(neg)