class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check_letter = {}

        for d in magazine:
            if d in check_letter:
                check_letter[d] = check_letter[d] + 1
            else:
                check_letter[d] = 1

        for d in ransomNote:
            if d not in check_letter:
                return False
            if check_letter[d] == 1:
                del check_letter[d]
            else:
                check_letter[d] -= 1

        return True