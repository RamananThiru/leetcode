"""

Insert a node at front in linked list
April 10, 2024
https://www.naukri.com/code360/problems/insert-node-at-the-beginning_8144739?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
"""


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Do not change code above.


def insertAtFirst(list: Node, newValue: int) -> Node:

    new_node = Node(newValue, list)


    return new_node
