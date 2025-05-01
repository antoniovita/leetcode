class Solution(object):
    def plusOne(self, digits):
        String = "".join(map(str, digits))
        NumberPlusOne = int(String) + 1
        StringPlusOne = str(NumberPlusOne)

        arrayAnswer = []
        for char in StringPlusOne:
            arrayAnswer.append(int(char))  
        return arrayAnswer


sol = Solution()
print(sol.plusOne([1, 2 ,3]))