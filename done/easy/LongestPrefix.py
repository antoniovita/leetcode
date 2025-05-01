from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arrayWordLen = []
        for word in strs:
            arrayWordLen.append(len(word))
        minWordCount = min(arrayWordLen)
        indexMinWord = arrayWordLen.index(minWordCount)

        prefix = strs[indexMinWord]

        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix



sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))