# using reverse operation
arr =[1,2,3,4,5,6]
k=3
arr.reverse()
arr[:k] = reversed(arr[:k])
arr[k:] = reversed(arr[k:])
print(arr)
# without reverse operation by swapping 
i=0
j=len(arr)-1
while i < j:
    arr[i],arr[j] = arr[j],arr[i]
    i+=1
    j-=1
i = 0
j= k-1
while i < j:
    arr[i],arr[j] = arr[j],arr[i]
    i+=1
    j-=1
i = k
j= len(arr)-1
while i < j:
    arr[i],arr[j] = arr[j],arr[i]
    i+=1
    j-=1
print(arr)