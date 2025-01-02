class Solution:
    def reverseWords(self, s: str) -> str:
        string_buffers = []
        start = -1
        i = 0

        while i < len(s):
            if s[i] != ' ':
                start = i
                while i+1< len(s) and s[i+1] != ' ':
                    i+=1
                string_buffers.append(s[start:i+1])
                start = i
            i +=1

        return ' '.join(string_buffers[::-1])