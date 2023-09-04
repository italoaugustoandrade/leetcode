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
                node.left=TreeNode(nums.pop(0))
                node.right=TreeNode(nums.pop(0))
                fila.append(node.left)
                fila.append(node.right)
        
        return root


class Solution:
    def maxDepth(self, root:[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


# Função para imprimir a árvore (para fins de teste

# Exemplo de uso:
nums_list = [3,9,20,None,None,15,7]
root1 = TreeNode.list_to_tree(nums_list)
solve = Solution()
a=solve.maxDepth(root1)
print(a)
# Imprime a árvore em ordem

