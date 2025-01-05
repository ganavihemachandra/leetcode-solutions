# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        graph = defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                graph[node.left].append(node)
                graph[node].append(node.left)
                q.append(node.left)
            if node.right:
                graph[node.right].append(node)
                graph[node].append(node.right)
                q.append(node.right)
        
        res = []
        q = deque([(target, 0)])
        path = set([target])

        while q:
            node, distance = q.popleft()
            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in path:
                        path.add(edge)
                        q.append((edge, distance + 1))
        return res
        
