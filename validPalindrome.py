class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = []
        for char in s:
            if char.isalpha():
                array.append(char.lower())
        return array == array[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
