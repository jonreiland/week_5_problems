import trees


class Solution:
    def max_val(self, root: trees.TreeNode) -> int:
        if root is None:
            return 0
        left_max = self.max_val(root.left)
        right_max = self.max_val(root.right)
        return max(root.val, left_max, right_max)


if __name__ == "__main__":
    sol = Solution()
    print(sol.max_val(trees.tree_a))
    print(sol.max_val(trees.tree_b))
    print(sol.max_val(trees.tree_c))
    print(sol.max_val(trees.tree_d))
    print(sol.max_val(trees.tree_e))
