class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        maxi = 0
        arr = []
        d = collections.defaultdict(lambda: 0)
        while len(q) > 0:
            front = q.popleft()
            d[front.val] += 1
            if d[front.val] > maxi:
                maxi = d[front.val]
                arr = [front.val]
            elif d[front.val] == maxi:
                arr.append(front.val)
            if front.left: 
                q.append(front.left)
            if front.right:
                q.append(front.right)
        return arr