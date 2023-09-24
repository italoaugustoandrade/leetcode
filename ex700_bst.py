''' 
700. Search in a Binary Search Tree


Ítalo Andrade
'''

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree(nums: List[int]):
        if not nums:
            return None

        root = TreeNode(nums.pop(0))
        fila = [root]

        while nums:
            node = fila.pop(0)
            if node is not None:
                node.left = TreeNode(nums.pop(0))
                if nums == []:
                    return root
                node.right = TreeNode(nums.pop(0))
                fila.append(node.left)
                fila.append(node.right)

        return root


class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    @staticmethod
    def rightSideView(root: [TreeNode]) -> List[int]:
        next = root
        count = []
        nivel=0
        if next is None:
            return None
        pilha = [[next,0]]
        while pilha:
            if nivel == len(count):
                count.append(next.val)
            if next.right is not None:
                pilha.append((next.right,nivel+1))
            if next.left is not None:
                pilha.append((next.left,nivel+1))
            
            next,nivel=pilha.pop(0)

        return count
    
    def searchBSTList(self, root: [TreeNode], val: int) -> [TreeNode]:
        next = root        
        nivel=0
        find = None
        path=[]
        if next is None:
            return None
        pilha = [[next,0]]

        while pilha:
            next,nivel=pilha.pop(0)
            if next.val == val:
                find=next
                pilha = []

            if find is not None:
                path.append(next.val)

            if next.left is not None:
                pilha.append((next.left,nivel+1))
            if next.right is not None:
                pilha.append((next.right,nivel+1))

            

        return path

    def searchBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        next = root        
        nivel=0
        if next is None:
            return None
        pilha = [[next,0]]

        while pilha:
            next,nivel=pilha.pop(0)
            if next.val == val:
                return next
            if next.left is not None:
                pilha.append((next.left,nivel+1))
            if next.right is not None:
                pilha.append((next.right,nivel+1))
        return None
    
    def deleteNode(self, root: [TreeNode], key: int) -> [TreeNode]:
        next = root        
        nivel=0
        if next is None:
            return None
        pilha = [[next,0]]

        while pilha:
            next,nivel=pilha.pop(0)
            if next.val == key:
                return next

            if next.left:
                pilha.append((next.left,nivel+1))
            if next.right:
                pilha.append((next.left,nivel+1))

        return None


    def deleteNode_error(self, root: [TreeNode], key: int) -> [TreeNode]:
        next = root        
        nivel=0
        find=None
        if next is None:
            return None
        pilha = [[next,next]]

        while pilha:
            next,ant=pilha.pop(0)
            if next.val == key:
                find=next
                if next.right is not None and next.left is None:
                    next.val=next.right.val
                    next.right=next.right.right
                elif next.right is not None and next.left is not None:
                    ant =next
                    next=next.right
                    while next is not None:
                        if next.left is not None:
                            ant=next
                            next=next.left
                        elif next.right is not None:
                            ant = next
                            next=next.right
                        else:
                            if next==ant.left:
                                ant.left=None
                            elif ant.right==next:
                                ant.right=None
                            find.val=next.val
                            break
                else:
                    if next==ant.left:
                        ant.left=None
                    elif ant.right==next:
                        ant.right=None
                    else:
                        return None
                return  root
            if next.left is not None:
                pilha.append((next.left, next))
            if next.right is not None:
                pilha.append((next.right, next))
        return root


null = None
nums_list = [5,3,6,2,4,null,7]
root1 = TreeNode.list_to_tree(nums_list)
solve = Solution()
valor=3
a = solve.deleteNode(root1,valor)
print(a)
