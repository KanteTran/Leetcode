# https://leetcode.com/problems/shifting-letters-ii/
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        max_code = ord('z')  # 122
        min_code = ord('a')  # 97
        moves = [0] * len(s)

        for step in shifts:
            move = 1 if step[2] == 1 else -1
            moves[step[0]] += move
            if step[1] + 1 < len(s):
                moves[step[1] + 1] -= move

        for i in range(1, len(moves)):
            moves[i] += moves[i - 1]

        out = ''
        for i in range(len(s)):
            tmp = (ord(s[i]) - min_code + moves[i]) % 26 + min_code
            out += chr(tmp)

        return out
