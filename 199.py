class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result  = []
        queue = collections.deque([root])
        while queue:
            rightSide = None
            qlen= len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                result.append(rightSide.val)
        return result
    
"""Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []"""