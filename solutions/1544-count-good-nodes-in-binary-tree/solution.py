# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 1 ---> DFS
        def dfs(node, maxVal):
            if not node:
                return 0
            
            count = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            return count + dfs(node.left, maxVal) + dfs(node.right, maxVal)
        return dfs(root, root.val)

        # 2 ---> bfs
        res = 0
        q = deque([(root, -float('inf'))])

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
            maxVal = max(maxVal, node.val)
            if node.left:
                q.append((node.left, maxVal))
            if node.right:
                q.append((node.right, maxVal))
        return res

