import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_binary_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    root.right.right.right.right = TreeNode(8)
    return root


class Solution:
    def __init__(self, root: TreeNode):
        self.preorder = self.preorder(root)
        self.inorder = self.inorder(root)
        self.postorder = self.postorder(root)
        self.level_order = self.level_order(root)

    def preorder(self, root: TreeNode) -> list:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, root: TreeNode, result: list) -> None:
        if root is None:
            return
        result.append(root.val)
        self._preorder(root.left, result)
        self._preorder(root.right, result)

    def inorder(self, root: TreeNode) -> list:
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, root: TreeNode, result: list) -> None:
        if root is None:
            return
        self._inorder(root.left, result)
        result.append(root.val)
        self._inorder(root.right, result)

    def postorder(self, root: TreeNode) -> list:
        result = []
        self._postorder(root, result)
        return result

    def _postorder(self, root: TreeNode, result: list) -> None:
        if root is None:
            return
        self._postorder(root.left, result)
        self._postorder(root.right, result)
        result.append(root.val)

    def level_order(self, root: TreeNode) -> list:
        result = []
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            result.append(curr.val)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return result


if __name__ == "__main__":
    sol = Solution(get_binary_tree())
    print(sol.preorder)
    print(sol.inorder)
    print(sol.postorder)
    print(sol.level_order)
