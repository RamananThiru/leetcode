'''

Problem: Suppose there is a string 'abcabc' . The longest repeating string is abc

if there is a string 'abcdabc' return -1 as d is in between


Examples:

Input: 'abcabc'
output: 'abc'


Input: 'abcdabc'
output: -1
'''

class Solution:
  def longest_valid_substring(self, input_string: str):
    length = len(input_string)
    longest = -1

    # substring cannot be a length greater than half of a string
    for itr in range(1, length//2 + 1):
      subString = input_string[:itr]

      if subString * length//itr == input_string:
        longest = subString
    
    return longest