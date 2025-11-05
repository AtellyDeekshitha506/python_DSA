nums = [23,4,567,634,67,4]
largest = nums[0]
second_largest = nums[0]
for i in range (len(nums)):
    if nums[i] > largest :
        largest = nums[i]
nums.remove(largest)
for i in range (len(nums)):
    if nums[i] > second_largest:
        second_largest = nums[i]
print(second_largest)