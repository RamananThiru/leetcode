"""

https://www.naukri.com/code360/problems/introduction-to-linked-list_8144737?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

April 10, 2024
"""




class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.


def constructLL(arr: [int]) -> Node:
    if len(arr) == 0:
        return

    linked_list = Node(arr[0])
    temp_head = linked_list

    for i in range(1, len(arr)):
       
        new_node = Node(arr[i])
        temp_head.next = new_node
        temp_head = new_node

    return linked_list
