

# Leetcode link: https://leetcode.com/problems/longest-consecutive-sequence/

# Time complexity is O(n) , eventhough loop within a loop is there
# This is a intresting solution of using two loops and not O(n^2) time complexity

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_hash  = Counter(nums)
        num_set = num_hash.keys() # Can also use num_set = set(nums) , no need to form hash 
        # i tried with the hash.keys() because , most times set(nums) sorted the nums array from [0,3,7,2,5,8,4,6,0,1] ->  {0, 1, 2, 3, 4, 5, 6, 7, 8}

        
        for n in num_set:
            # n-1 is considered as , if we encounter with 2 and if 1 is present , the longest would start from 1 and be 1,2 . it won't be 2,3 . But 1,2,3 would be the longest
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest
