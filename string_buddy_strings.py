

# April, 6,7 2024

 
 """
  https://leetcode.com/problems/buddy-strings/
  
  Psuedo Code
  
  Two base cases : If string is same and string is not same

  -> When strings are equal (Hashing)
    If string is same , if there exists atleast one duplicate characters , duplicate characters can be swapped to get the same string again. i.e any value of hash >= 2 . 
    If string is same , and there are no duplicate characters , it is not possible to swap two different characters and get the same string  i.e NO value of hash >= 2

  -> When strings are not equal:
    Brute force Approach (Two for loops)
      - Compare the char at index 0 with characters i all other indices of the same string till you get the 'goal' string

    Optimised Solution:  (comparing the character present in same index of 's' and 'goal'
      - whenever a character doesn't match add the index to an array 'diff_index' 
      - If there are more than 2 characters  difference , same string cannot be achieved by just swapping characters from two indices

 """


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False

        # Swap characters within the same string

        if s == goal:
            s_hash = self.countFrequency(s)
            max_freq = max(s_hash.values())

            if max_freq > 1:
                return True
            else:
                return False    
        
        diff_index = [] # Find the different indeces comparing both the string

        for i in range(0,len(s)):
            if s[i] != goal[i]:
                diff_index.append(i)

        if len(diff_index) !=2:
            return False        

        temp_str = s
        input_str = self.form_string_and_swap(temp_str, diff_index[0], diff_index[1])


        return input_str == goal            



    def form_string_and_swap(self, input_string, i, j):
        char_arr = list(input_string)

        temp = char_arr[i]
        char_arr[i] =  char_arr[j]
        char_arr[j] = temp

        return ''.join(char_arr)

    def countFrequency(self , word):
        hash = {}

        for i in word:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1       
        return hash    
        
        
                      
