from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        move = [0 for _ in s]
        for start, end, direct in shifts:
            move[start] += 1 if direct == 1 else -1
            if end < len(s) - 1:
                move[end+1] -= 1 if direct == 1 else -1
        for k in range(1, len(s)):
            move[k] = move[k] + move[k-1]

        res = ''
        for d in range(len(s)):
            res += chr((ord(s[d]) - ord('a') + move[d])%26 + ord('a'))  # ord('a') = 97, ord('z') = 122

        return res


if __name__ == '__main__':
    s = "dztz"
    shifts = [[0,0,0],[1,1,1]]
    print(Solution().shiftingLetters(s, shifts))  # "bac"