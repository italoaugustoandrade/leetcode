''' 
199. Binary Tree Right Side View

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





# Função para imprimir a árvore (para fins de teste

# Exemplo de uso:
null = None
nums_list = [1,2,3,4]
root1 = TreeNode.list_to_tree(nums_list)
solve = Solution()
a = solve.rightSideView(root1)
print(a)
# Imprime a árvore em ordem
