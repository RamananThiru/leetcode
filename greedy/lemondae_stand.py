# Problem: https://leetcode.com/problems/lemonade-change/
from typing import List

'''
Input: [5,5,5,10,20]


Input can have only valid bill values so 5$ , 10$ and 20$ being the maximum. So we used if else statements
'''



class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = count_ten = 0 

        for bill in bills:
            if bill == 5:
                count_five += 1
            
            elif bill == 10:
                if count_five > 0:
                    count_five -= 1
                    count_ten += 1
                else:
                    return False
            else: # only 20 is considered as valid bill values. i.e 15, 25 are not valid
                if count_ten and count_five:
                    count_ten -= 1
                    count_five -= 1
                elif count_five >=3:
                    count_five -= 3
                else:
                    return False
        return True

        