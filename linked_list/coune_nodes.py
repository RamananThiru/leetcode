'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    count = 1

    while(head.next is not None):
        count += 1
        head = head.next


    return count    
