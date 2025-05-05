class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = x**(1/2)
        return int(sqrt)
    
sol = Solution()
print(sol.mySqrt(8))