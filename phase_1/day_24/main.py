# https://leetcode.com/problems/word-subsets
class Solution:
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        out = []
        full_s = ''.join(words2)
        arr = []
        freq_2 ={}
        for w in words2:
            arr.append(count_freq(w))
        for obj in arr:
            for k,v in obj.items():
                if freq_2.get(k):
                    freq_2[k] = max(freq_2[k], v)
                else:
                    freq_2[k] = v
        for s in words1:
            freq_1 = count_freq(s) 
            if all(freq_1.get(c, 0) >= f for c, f in freq_2.items()):
                out.append(s)
        return out
    
def count_freq(s):
        freq = {}
        for c in s:
            if freq.get(c):
                freq[c] += 1
            else:
                freq[c] = 1
        return freq
        
        