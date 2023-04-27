''' 
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1
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
    def middleNode(head: ListNode) -> ListNode:
        """Given the head of a singly linked list, return the middle node of the linked list.

        If there are two middle nodes, return the second middle node.

        Returns:
            ListNode: Middlist
        """
        current = head
        middle = current
        array_val = []
        # Input processing: None type
        i = 1
        j = 1
        if head is None:
            return

        while True:

            if current.next is None:
                array_val.append(current.val)
                if i%2==0:
                    middle=middle.next
                return middle


            if j*2 <= i:
                j = j+1
                middle=middle.next
            array_val.append(current.val)
            current = current.next
            i = i+1



list3 = ListNode.create_linked_list(array_list=[1, 2, 3, 4, 5, 6, 8,9])
list4 = ListNode.create_linked_list(array_list=[0])


resultado = Solution.middleNode(list3)
resultado.print_linked_list()
