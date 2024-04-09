"""

"""


"""

Solution 1:
Time limit execeded , logic correct

Logic:

take [1,2,3,4]

iteration 1: nums = [24, 2, 3,4]  and after nums is changed temp = 1 (Removed the element from the current index and store it) [ product of elements to the right = 4 * 3 *2 ] since there is no element to left , it is 4 *3 * 2 *1 , where temp = 1
iteration 2: nums = [24, 12 , 3 4] , => temp = 2. => 4 * 3 * temp = 12

....

last iteration with index = len(nums) - 1. It is only the products of elements in the left , so nums[len(num)-1] = temp => nums[3] = 6
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1

        for i in range(0, len(nums)):
            mul_result =  self.calculateModifyNums(nums, temp, i)
            temp = temp * nums[i]
            nums[i] =  mul_result
            
        return nums    
        


    def calculateModifyNums(self, tmp_arr, temp, index):
        mul = 1

        if index == len(tmp_arr) - 1:
            return temp

        for j in range(index+1, len(tmp_arr)):
            mul = mul * tmp_arr[j]

        return mul * temp        
       


"""

Solution 2:
"""

