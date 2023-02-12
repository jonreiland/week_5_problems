import trees


class Solution:
    def height(self, root: trees.TreeNode) -> int:
        if root is None:
            return -1
        left_height = self.height(root.left) + 1
        right_height = self.height(root.right) + 1
        return max(0, left_height, right_height)


if __name__ == "__main__":
    sol = Solution()
    print(sol.height(trees.tree_a))
    print(sol.height(trees.tree_b))
    print(sol.height(trees.tree_c))
    print(sol.height(trees.tree_d))
    print(sol.height(trees.tree_e))
