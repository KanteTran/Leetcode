# https://leetcode.com/problems/string-matching-in-an-array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    out.append(words[i])
                    break
        return out
                    