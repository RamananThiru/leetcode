class Solution:
    def isValid(self, s: str) -> bool:
      arr = []
      arr.append(s[0])
      for i in range(1,len(s)):
        if s[i] == '{' or  s[i] == '[' or s[i] == '(':
          arr.append(s[i])
        elif s[i] == '}':
          if  len(arr) != 0 and arr[-1] == '{':
            arr.pop()
          else:
            arr.append(s[i])
        elif s[i] == ']':
          if  len(arr) != 0 and arr[-1] == '[':
            arr.pop()
          else:
            arr.append(s[i])

        elif s[i] == ')':
          if len(arr) != 0 and arr[-1] == '(':
            arr.pop()
          else:
            arr.append(s[i])
        
      if len(arr) == 0:
        return True
      else:
        return False
          
          
      
      