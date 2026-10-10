class Solution:
    def isValid(self, s: str) -> bool:

        Brackets = {')': '(', '}': '{', ']' :'['}
        stack = []

        for char in s:
            if char in Brackets:
                if stack and stack[-1] == Brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
                



        