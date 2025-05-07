class Solution(object):
    def addBinary(self, a, b):
        int_a = int(a, 2)
        int_b = int(b, 2)

        total = int_a + int_b

        return bin(total)[2:]


sol = Solution()
print(sol.addBinary("10101" , "11"))