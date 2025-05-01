class Solution(object):
    def findNumbers(self, nums):
        cont = 0 
        for num in nums:
            strNum = str(num)
            if len(strNum) % 2 == 0:
                cont +=1
        return cont

sol = Solution()
print(sol.findNumbers([12,345,2,6,7896]))