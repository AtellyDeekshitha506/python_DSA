class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                return left+1, right+1 
            elif total < target:
                left += 1
            else:
                right -= 1
nums = [2,3,4]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))