



class Solution:
    
    def __init__(self):
        self.nums = [4,3,6,5,1,2]
        
    def sortStack(self):
        if self.nums:
            curr_element = self.nums.pop()
            self.sortStack()
            self.insert_stack_sort(curr_element)
        return self.nums    
        
        
    def insert_stack_sort(self, top):
        if not self.nums or top > self.nums[-1]:
            self.nums.append(top)
            return 
        
        temp = self.nums.pop()
        self.insert_stack_sort(top)
        self.nums.append(temp)


obj =  Solution()
print(obj.sortStack())
