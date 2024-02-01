class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) % 2:
            return False

        __paran_check = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        __stack = []
        for i in s:
            if __stack and i in __paran_check:
                if __stack[-1] == __paran_check[i]:
                    __stack.pop()
                else:
                    return False
            else:
                __stack.append(i)

        return __stack == []
