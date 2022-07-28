#28th july 2022
#reference link: 
#https://leetcode.com/problems/longest-common-prefix/discuss/2345680/C%2B%2B-or-Easy-to-Undestand-or-Clean-Code-or-Best-Method

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #return if the list is empty 
        if len(strs) == 0:
          return ''
        if len(strs) == 1:
          return strs[0]
        
        min = 1000000000 
        result = ''
        #find the shortest word from the array of strings
        for i in range(len(strs)):
          if strs[i] == '':
            return ''
          if len(strs[i]) < min:
            min = len(strs[i])
        
        for i in range(0, min):
          for j in range(0, len(strs)-1):
            if strs[j][i] != strs[j+1][i]:
              return result
          result = result + strs[j][i]
        return result