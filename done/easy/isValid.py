class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "({[":
                stack.append(char)  
            elif char in ")}]":
                if not stack or stack[-1] != pair[char]:
                    return False
                stack.pop() 

        return len(stack) == 0

sol = Solution()
print(sol.isValid("((()))"))
    

