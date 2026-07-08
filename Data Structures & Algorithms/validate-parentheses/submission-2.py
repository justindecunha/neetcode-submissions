class Solution:
    def isValid(self, brackets: str) -> bool:
        
        s = []

        for z in brackets:
            if z == '(':
                s.append(')')
            elif z == '[':
                s.append(']')
            elif z == '{':
                s.append('}')
            else:
                if not s or z != s.pop():
                    return False
        
        return not s