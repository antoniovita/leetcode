class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))