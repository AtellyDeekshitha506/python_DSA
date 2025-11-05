
arr = [1,2,3,1,2,34,4,5,2]
new_array = []
for i in range(len(arr)):
    if arr[i] not in new_array:
        new_array.append(arr[i])
print(new_array)

nums = [1,1,2,2,3,3]
left = 0
while left < len(nums)-1:
    if nums[left] == nums[left+1]:
        nums.pop(left+1)
    else:
        left+=1
print(nums)