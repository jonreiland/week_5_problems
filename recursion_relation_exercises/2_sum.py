import trees


class Solution:
    def sum(self, root: trees.TreeNode) -> int:
        """Finds the sum of nodes in a binary tree."""
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)


if __name__ == "__main__":
    sol = Solution()
    print(sol.sum(trees.tree_a))
    print(sol.sum(trees.tree_b))
    print(sol.sum(trees.tree_c))
    print(sol.sum(trees.tree_d))
    print(sol.sum(trees.tree_e))
