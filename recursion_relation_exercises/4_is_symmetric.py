import trees
import collections


class Solution:
    def is_symmetric(self, root: trees.TreeNode) -> bool:
        queue = collections.deque([root])
        levels = []
        curr_level = []
        next_level = []
        while queue:
            curr = queue.popleft()
            curr_level.append(curr.val)
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
            if len(queue) == 0:
                levels.append(curr_level)
                curr_level = []
                queue.extend(next_level)
                next_level = []

        for i, level in enumerate(levels):
            if i == 0:
                continue
            if len(level) < 2 and i > 0:
                return False
            if len(level) % 2 != 0:
                return False
            left = level[:len(level)//2]
            right = level[len(level)//2:]
            left.reverse()
            for i in range(len(left)):
                if left[i] != right[i]:
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_symmetric(trees.tree_a))
    print(sol.is_symmetric(trees.tree_b))
    print(sol.is_symmetric(trees.tree_c))
    print(sol.is_symmetric(trees.tree_d))
    print(sol.is_symmetric(trees.tree_e))
