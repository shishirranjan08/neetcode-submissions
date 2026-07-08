class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        for item in s:
            if item == "(" or item  == "{" or item == "[" :
                stack.append(item)
            elif item == ")" and stack:
                if stack.pop() != "(":
                    return False
            elif item == "}" and stack:
                if stack.pop() != "{":
                    return False
            elif item == "]" and stack:
                if stack.pop() != "[":
                    return False
            else:
                return False
            
        return len(stack) == 0