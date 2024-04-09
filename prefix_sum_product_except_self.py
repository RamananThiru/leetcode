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

Have two arrays , one array that calculates the prefix from product from left to right 
Another array , that calculates the prefix product from right to left
"""



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        # Calculate left prefix product
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Calculate right suffix product
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(left, right)    

        # Calculate result array
        result = [left[i] * right[i] for i in range(n)]
       
        return result

