class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        minstr = a if len(a)<len(b) else b
        maxstr = a if len(a)>=len(b) else b
        minlen = min(len(a), len(b))
        maxlen = max(len(a), len(b))
        prevbit = 0
        for i in range(maxlen):
            expr = ((int(minstr[-i-1]) if i < minlen else 0) + int(maxstr[-i-1]) + prevbit)
            answer.append(str(expr % 2))
            prevbit = expr // 2
        if prevbit == 1:
            answer.append('1')
        return ''.join(answer[::-1])