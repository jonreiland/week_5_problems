import trees


class Solution:
    def leafs(self, root: trees.TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        num_leafs = 0
        if root.left:
            num_leafs += self.leafs(root.left)
        if root.right:
            num_leafs += self.leafs(root.right)
        return num_leafs


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    for tree in binary_trees:
        sol = Solution()
        print(sol.leafs(tree))
