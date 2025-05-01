class Solution:
    def isPalindrome(self, x: int) -> bool:
        numberString = str(x)
        reverse = numberString[::-1]

        if reverse == numberString:
            return True
        else:
            return False
        
sol = Solution()
resultado = sol.isPalindrome(121)
print(resultado)
        
        