class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        counta = countb = 0
        res = ""

        for _ in range(a + b):
            if (a > b and counta < 2) or countb == 2:
                res += "a"
                counta, countb = counta + 1, 0
                a -= 1
            else:
                res += "b"
                countb, counta = countb + 1, 0
                b -= 1

        return res

