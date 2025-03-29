class Solution(object):
    def isValid(self, s):
        stack =[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i] ==')':
                if not stack:
                    return False
                last = stack.pop()
                if last!='(':
                    return False
            elif s[i] =='}':
                if not stack:
                    return False
                last = stack.pop()
                if last!='{':
                    return False
            elif s[i]==']':
                if not stack:
                    return False
                last = stack.pop()
                if last!='[':
                    return False
        if not stack:
            return True
        else:
            return False
            
                
   
        