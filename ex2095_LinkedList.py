''' 
2095. Delete Middle

Ítalo Andrade

'''
from typing import List


class ListNode:
    """Class Node for singly-linked list
    """

    def __init__(self, val=0, next=None):  # pylint: disable=W0622
        # Var next defined by question
        self.val = val
        self.next = next

    @staticmethod
    def create_linked_list(array_list):
        """Create a linked list from a list or tuple

        Args:
            array_list (tuple or list): data to be transformed in a linked list.

        Returns:
            linked_list: A ListNode linked with all data from arraylist. 
        """
        current_node = ListNode()
        linked_list = current_node
        for i, value in enumerate(array_list):
            current_node.val = value
            if i < len(array_list)-1:
                current_node.next = ListNode()
                current_node = current_node.next

        return linked_list

    def print_linked_list(self):
        """
        Print the data from a liked_list
        """
        current = self
        while current.next is not None:
            print(current.val)
            current = current.next
        print(current.val)
        return


class Solution:
    """Class Solution for question.

    Returns:
        None
    """

    @staticmethod
    def deleteMiddle(head: [ListNode]) -> [ListNode]:
        i = 0
        mid = 0
        prox = head
        while prox.next is not None:
            i = i+1
            prox = prox.next
        if i % 2 == 0:
            mid = int(i/2)
        else:
            mid = int(i/2)+1
        i = 0
        prox = head
        while mid > 0:
            if i == mid-1:
                descart = prox.next
                prox.next = descart.next
                return head

            else:
                i = i+1
                prox = prox.next
        return head


list3 = ListNode.create_linked_list(array_list=[1])
solve = Solution.deleteMiddle(list3)
ListNode.print_linked_list(solve)
