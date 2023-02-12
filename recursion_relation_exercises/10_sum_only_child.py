import trees


class Solution:
    def __init__(self):
        self.result = 0

    def sum_only_child(self, root: trees.TreeNode) -> None:
        if root is None:
            return

        if root.left and root.right is None:
            self.result += 1
            self.sum_only_child(root.left)
            return

        if root.right and root.left is None:
            self.result += 1
            self.sum_only_child(root.right)
            return

        self.sum_only_child(root.left)
        self.sum_only_child(root.right)


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    for tree in binary_trees:
        sol = Solution()
        sol.sum_only_child(tree)
        print(sol.result)
