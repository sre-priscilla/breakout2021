class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        # 或进或出
        for ch in s:
            if len(stack) > 0 and pairs.get(stack[-1], '') == ch:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack) == 0
