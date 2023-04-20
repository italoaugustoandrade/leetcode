''' 
Question 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

Ítalo Andrade

'''


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
    """
     Class Solution for question. 
    """
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Args:
            l1 (ListNode): ListNode to add
            l2 (ListNode): ListNode to add

        Returns:
            lout (ListNode): ListNode added 
        """
        rest = 0
        value = 0
        current = ListNode()
        lout = current
        while 1:
            value = (l1.val+l2.val+rest) % 10
            current.val = value
            rest = (l1.val+l2.val+rest)//10
            if l1.next is None and l2.next is None:
                if rest > 0:
                    current.next = ListNode()
                    current = current.next
                    current.val = rest
                return lout
            l1.val = 0
            l2.val = 0
            l1 = l1.next if l1.next is not None else l1
            l2 = l2.next if l2.next is not None else l2
            current.next = ListNode()
            current = current.next


list1 = ListNode.create_linked_list(array_list=[2, 4, 3, 1])
list2 = ListNode.create_linked_list(array_list=[2, 9, 9])
list3 = ListNode.create_linked_list(array_list=[9, 9, 9, 9, 9, 9, 9])
list4 = ListNode.create_linked_list(array_list=[9, 9, 9, 9])

resultado = Solution.addTwoNumbers(list3, list4)
resultado.print_linked_list()
