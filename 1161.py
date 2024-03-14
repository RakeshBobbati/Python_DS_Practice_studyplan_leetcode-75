class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        level = 1
        queue = collections.deque([root])
        prev_level_sum = -math.inf
        while queue:
            qlen = len(queue)
            curr_sum = 0
            for i in range(qlen):
                node = queue.popleft()
                curr_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if prev_level_sum < curr_sum:
                prev_level_sum = curr_sum
                ans = level
            level+=1
        return ans
    
"""Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2"""