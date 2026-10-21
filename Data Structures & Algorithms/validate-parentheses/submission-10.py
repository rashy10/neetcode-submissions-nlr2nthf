class Solution:
    def isValid(self, s: str) -> bool:
        map = {")":"(" , "}":"{" , "]":"["}

        stack = []
        for c in s:
            if (c in map )and stack:
                if  stack[-1] == map[c] :
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        print(stack)
        if stack:
            return False
        return True
            

        