''' 
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan&id=level-1
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
    def detectCycle(head: ListNode) -> ListNode:
        """Given the head of a linked list, return the node where the cycle begins. 
        If there is no cycle, return null.

        There is a cycle in a linked list if there is some node in the list that can be 
        reached again by continuously following the next pointer. Internally, pos is used 
        to denote the index of the node that tail's next pointer is connected to (0-indexed). 
        It is -1 if there is no cycle. Note that pos is not passed as a parameter.

        Do not modify the linked list.

        Returns:
            int: pos
        """
        current = head
        key_hash = {}
        i = 0
        # Input processing: None type

        if head is None:
            return

        while True:

            if current in key_hash:
                return current

            if current.next is None:
                return
            key_hash[current] = current.val
            current = current.next
            i = i+1


list3 = ListNode.create_linked_list(array_list=[-1,-7,7,-4,19,6,-9,-5,-2,-5])
list4 = ListNode.create_linked_list(array_list=[0])


resultado = Solution.detectCycle(list3)
resultado.print_linked_list()
