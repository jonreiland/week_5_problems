import trees


class Solution:
    def full(self, root: trees.TreeNode) -> bool:
        if root is None:
            return True

        if root.left and root.right is None:
            return False

        if root.right and root.left is None:
            return False

        return self.full(root.left) and self.full(root.right)


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    for tree in binary_trees:
        sol = Solution()
        print(sol.full(tree))
