import trees


class Solution:
    def __init__(self):
        self.diameter = 0

    def find_diameter(self, root: trees.TreeNode):
        if root is None:
            return 0

        self.diameter = max(self.diameter,
                            self.height(root.left) + 1 +
                            self.height(root.right) + 1)
        self.find_diameter(root.left)
        self.find_diameter(root.right)

    def height(self, root: trees.TreeNode) -> int:
        if root is None:
            return -1
        left_height = self.height(root.left) + 1
        right_height = self.height(root.right) + 1
        return max(0, left_height, right_height)


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    for tree in binary_trees:
        sol = Solution()
        sol.find_diameter(tree)
        print(sol.diameter)
