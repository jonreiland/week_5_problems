import trees


class Solution:
    def same(self, root_a: trees.TreeNode, root_b: trees.TreeNode) -> None | bool:
        if root_a is None or root_b is None:
            return
        if root_a.val != root_b.val:
            return False
        left_res = self.same(root_a.left, root_b.left)
        right_res = self.same(root_a.right, root_b.right)
        if left_res is False or right_res is False:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.same(trees.tree_a, trees.tree_a))
    print(sol.same(trees.tree_a, trees.tree_b))
    print(sol.same(trees.tree_b, trees.tree_b))
    print(sol.same(trees.tree_b, trees.tree_c))
    print(sol.same(trees.tree_c, trees.tree_c))
    print(sol.same(trees.tree_c, trees.tree_d))
    print(sol.same(trees.tree_d, trees.tree_d))
    print(sol.same(trees.tree_d, trees.tree_e))
    print(sol.same(trees.tree_e, trees.tree_e))
    print(sol.same(trees.tree_e, trees.tree_a))
