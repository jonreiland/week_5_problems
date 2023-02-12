import trees


class Solution:
    def top_ordered(self, root: trees.TreeNode) -> bool:
        """Recursive function that returns true if all root nodes are
        smaller than their left and right children.
        """
        if root.left is None and root.right is None:
            return True

        if root.left and root.right:
            if root.left.val < root.val or root.right.val < root.val:
                return False
            else:
                return self.top_ordered(root.left) and \
                       self.top_ordered(root.right)

        if root.left:
            if root.left.val < root.val:
                return False
            else:
                return self.top_ordered(root.left)

        if root.right:
            if root.right.val < root.val:
                return False
            else:
                return self.top_ordered(root.right)


if __name__ == "__main__":
    binary_trees = [trees.tree_a, trees.tree_b, trees.tree_c,
                    trees.tree_d, trees.tree_e]
    sol = Solution()
    for tree in binary_trees:
        print(sol.top_ordered(tree))
