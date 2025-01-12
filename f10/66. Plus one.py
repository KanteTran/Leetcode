class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        add = 1
        for i,d in enumerate(digits):
            if digits[i] < 9:
                digits[i] += add
                return digits[::-1]
            else:
                digits[i] = 0

        if add == 1:
            digits.append(1)

        return digits[::-1]