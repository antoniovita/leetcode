class Solution(object):
    def addTwoNumbers(self, l1, l2):
        invertedL1= l1[::-1]
        invertedL2 = l2[::-1]

        numberedInvertedL1 = int("".join(map(str, invertedL1)))
        numberedInvertedL2 = int("".join(map(str, invertedL2)))

        return numberedInvertedL1 + numberedInvertedL2

sol = Solution()
resultado = sol.addTwoNumbers([2, 4 ,3 ], [5, 6 ,4])
print(resultado)