import trees


class Solution:
    def __init__(self):
        self.result = 0

    def find_height(self, root: trees.TreeNode, height: int) -> None:
        if height == 0:
            self.result += 1
            return

        if root.left:
            self.find_height(root.left, height-1)

        if root.right:
            self.find_height(root.right, height-1)


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    for tree in binary_trees:
        sol = Solution()
        sol.find_height(tree, 2)
        print(sol.result)
