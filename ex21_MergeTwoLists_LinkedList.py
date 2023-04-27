''' 
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1
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
    def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        """
        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists in a one sorted list. The list should be made by 
        splicing together the nodes of the first two lists.

        Return the head of the merged linked list.
        Args:
            l1 (ListNode): ListNode to merge
            l2 (ListNode): ListNode to merge

        Returns:
            (ListNode): Head of linked list 
        """
        current = ListNode()
        head = current
        MAX_VAL = 150  # MAX number input

        # Input processing: None type
        if list1 is None and list2 is None:
            return
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while True:
            if list1.val < list2.val:
                current.val = list1.val
                if list1.next is not None:  # Next node
                    list1 = list1.next
                else:  # Set upper limit
                    list1.val = MAX_VAL
            else:
                current.val = list2.val
                if list2.next is not None:  # Next node
                    list2 = list2.next
                else:  # Set upper limit
                    list2.val = MAX_VAL

            if list2.val == MAX_VAL and list1.val == MAX_VAL:  # When both list ended
                return head
            else:
                current.next = ListNode()
                current = current.next


list3 = ListNode.create_linked_list(array_list=[])
list4 = ListNode.create_linked_list(array_list=[0])


resultado = Solution.mergeTwoLists(list3, list4)
resultado.print_linked_list()
