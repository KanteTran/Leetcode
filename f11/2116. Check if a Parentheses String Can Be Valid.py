class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lenght = len(s)

        if lenght % 2 == 1: return False

        open_rackets = []
        unlocked = []

        for i in range(lenght):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == "(":
                open_rackets.append(i)
            elif s[i] == ")":
                if open_rackets:
                    open_rackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open_rackets and unlocked and open_rackets[-1] < unlocked[-1]:
            open_rackets.pop()
            unlocked.pop()

        if open_rackets:
            return False

        return True