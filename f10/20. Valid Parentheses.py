class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_parentheses = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for d in s:
            if d in ["(", "{", "["]:
                stack.append(d)
            else:
                if len(stack) == 0 or map_parentheses[d] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
