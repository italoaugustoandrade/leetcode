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
    def reverseList(head: ListNode) -> ListNode:
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
        current = head
        array_val = []
        # Input processing: None type

        if head is None:
            return

        while True:
            if current.next is None:
                array_val.append(current.val)
                break
            array_val.append(current.val)
            current = current.next

        current = ListNode()
        linked_list = current
        for i, value in enumerate(reversed(array_val)):
            current.val = value
            if i < len(array_val)-1:
                current.next = ListNode()
                current = current.next

        return linked_list


list3 = ListNode.create_linked_list(array_list=[1, 2])
list4 = ListNode.create_linked_list(array_list=[0])


resultado = Solution.reverseList(list3)
resultado.print_linked_list()
