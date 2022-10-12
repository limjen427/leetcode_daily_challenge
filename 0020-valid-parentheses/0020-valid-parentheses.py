class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        
        if len(s) % 2 != 0:
            return False
        
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i != dict[a]:
                    return False
        return stack == []
                