import collections


class NaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def get_nary_tree():
    root = NaryTreeNode(1)
    node_2 = NaryTreeNode(2)
    node_3 = NaryTreeNode(3)
    node_4 = NaryTreeNode(4)
    node_5 = NaryTreeNode(5)
    node_6 = NaryTreeNode(6)
    node_7 = NaryTreeNode(7)
    node_8 = NaryTreeNode(8)
    node_9 = NaryTreeNode(9)
    node_10 = NaryTreeNode(10)
    node_11 = NaryTreeNode(11)
    node_12 = NaryTreeNode(12)
    node_13 = NaryTreeNode(13)
    node_14 = NaryTreeNode(14)
    root.children.extend([node_2, node_3, node_4])
    node_2.children.extend([node_5])
    node_3.children.extend([node_6, node_7])
    node_6.children.extend([node_9])
    node_4.children.extend([node_8])
    node_8.children.extend([node_10, node_11])
    node_10.children.extend([node_12, node_13])
    node_11.children.extend([node_14])
    return root


class Solution:
    def __init__(self, root: NaryTreeNode):
        self.preorder = self.preorder(root)
        self.inorder = self.inorder(root)
        self.postorder = self.postorder(root)
        self.level_order = self.level_order(root)

    def preorder(self, root: NaryTreeNode) -> list:
        result = []
        self._preorder(root, result)
        return result

    def _preorder(self, root: NaryTreeNode, result: list) -> None:
        result.append(root.val)
        for child in root.children:
            self._preorder(child, result)

    def inorder(self, root: NaryTreeNode) -> list:
        result = []
        self._inorder(root, result)
        return result

    def _inorder(self, root: NaryTreeNode, result: list) -> None:
        for child in root.children[:-1]:
            self._inorder(child, result)
        result.append(root.val)
        if len(root.children) > 0:
            self._inorder(root.children[-1], result)

    def postorder(self, root: NaryTreeNode) -> list:
        result = []
        self._postorder(root, result)
        return result

    def _postorder(self, root: NaryTreeNode, result: list) -> None:
        for child in root.children:
            self._postorder(child, result)
        result.append(root.val)

    def level_order(self, root: NaryTreeNode) -> list:
        result = []
        queue = collections.deque([root])
        while queue:
            curr = queue.popleft()
            result.append(curr.val)
            queue.extend(curr.children)
        return result


if __name__ == "__main__":
    sol = Solution(get_nary_tree())
    print(sol.preorder)
    print(sol.inorder)
    print(sol.postorder)
    print(sol.level_order)
