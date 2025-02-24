
# Problem: https://leetcode.com/problems/jump-game/description/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0


        for index, num in enumerate(nums):
            # maximum index you can jump from current index
            max_index = max(max_index, index + num)

            # if you can jump to the end of the array or greater than the len of array. You have successfully jumped over
            if max_index >= len(nums) - 1:
                # added for cases like [2,0,0]
                return True

            # if i encounter an index with value 0 , if i have already passed this index means i am not blocked from moving past this 0 value index
            if num == 0 and max_index <= index:
                return False
        
        return True
        

        