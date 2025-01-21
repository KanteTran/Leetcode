class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.squares(n)

            if n == 1:
                return True

        return False


    def squares(self, n):
        ret_val = 0
        while (n) :
            ret_val += (n%10)**2
            n = n // 10
        return ret_val