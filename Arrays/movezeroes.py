# with extra array
nums =[0,1,2,0,3,0,0,0,3]
res=[]
count = 0
for i in range(len(nums)):
    if nums[i] != 0:
        res.append(nums[i])
    else:
        count +=1
for i in range(count):
    res.append(0)
print(res)
# without extra array
pos = 0
for i in range (len(nums)):
    if nums[i] != 0 :
        nums[pos] = nums[i]
        pos +=1
for i in range (pos,len(nums)):
    nums[i] = 0
print(nums)
