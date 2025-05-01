class Solution:
    def romanToInt(self, s: str) -> int:
        romanos = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and romanos[s[i]] < romanos[s[i + 1]]:
                total += romanos[s[i + 1]] - romanos[s[i]]
                i += 2
            else:
                total += romanos[s[i]]
                i += 1
        
        return total

sol = Solution()
print(sol.romanToInt("MCMXCIV"))