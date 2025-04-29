class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        for idx, num in enumerate(nums):
            complemento = target - num
            if complemento in seen:
                return [seen[complemento], idx]
            seen[num] = idx

sol = Solution()
resultado = sol.twoSum([1, 2, 3, 4], 4)
print(resultado)
