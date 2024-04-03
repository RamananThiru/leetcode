
# April 2,3 2024
# Resource https://www.enjoyalgorithms.com/blog/sort-stack-using-temporary-stack


# Description - Sort a stack using recursion
# Use a temp list to achieve , stack cannot be sorted by just using the parent stack list

# This solves only this case and other edge cases fails. Just to keep track of the solutions i wrote

stack = [4,3,6,5,1,2]
temp = []

def reverse_stack(stack, temp):
    while len(stack) > 0:
        print(stack, temp)
        curr_element = stack.pop()
        
        if len(temp) == 0 or curr_element >= temp[-1]:
            # print(stack, temp, curr_element)
            temp.append(curr_element)
        else:
            top_element = temp.pop()
            while(curr_element <= top_element):
                # print(stack, temp)  
                stack.append(top_element)
                if len(temp) == 0 or curr_element > temp[-1]:
                    break
                elif len(temp) != 0:
                    top_element = temp.pop()
            temp.append(curr_element)
          
    # print(temp) 
    
        
reverse_stack(stack, temp)



# Output Stack trace:

# [4, 3, 6, 5, 1, 2] []
# [4, 3, 6, 5, 1] [2]
# [4, 3, 6, 5, 2] [1]
# [4, 3, 6, 5] [1, 2]
# [4, 3, 6] [1, 2, 5]
# [4, 3] [1, 2, 5, 6]
# [4, 6, 5] [1, 2, 3]
# [4, 6] [1, 2, 3, 5]
# [4] [1, 2, 3, 5, 6]
# [6, 5] [1, 2, 3, 4]
# [6] [1, 2, 3, 4, 5]
