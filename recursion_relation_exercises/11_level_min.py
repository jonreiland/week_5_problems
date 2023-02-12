import trees


class Solution:
    def __init__(self):
        self.result = None

    def level_min(self, root: trees.TreeNode, height: int) -> int:
        if height == 0 and self.result is None:
            self.result = root.val
            return

        if root.left:
            self.level_min(root.left, height-1)

        if root.right:
            self.level_min(root.right, height-1)


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    for tree in binary_trees:
        sol = Solution()
        sol.level_min(tree, 2)
        print(sol.result)
