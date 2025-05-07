class Solution(object):
    def searchInsert(self, nums, target):
            if target in nums:
                return nums.index(target)
            else: 
                nums.append(target)
                nums = sorted(nums)
                return nums.index(target)
sol = Solution()
print(sol.searchInsert([1,3,5,6], 2))