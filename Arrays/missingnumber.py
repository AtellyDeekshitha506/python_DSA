arr = [1,2,4,5,6,7]
n = len(arr)+1
actual_sum = 0
excepted_sum =0
for i in range(len(arr)):
    actual_sum += arr[i]
excepted_sum = n*(n+1)//2
missing_num = excepted_sum - actual_sum
print(missing_num)