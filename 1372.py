class Solution:
    def __init__(self):
        self.ans = 0
    def testDFS(self,node,deep,side):
        self.ans =max(self.ans,deep)
        if node.left is not None:
            if side!= "left":
                self.testDFS(node.left,deep+1,"left") 
            else:
                self.testDFS(node.left,1,"left")

        if node.right is not None:
            if side!= "right":
                self.testDFS(node.right,deep+1,"right")
            else:
                self.testDFS(node.right,1,"right")   
        return 
        
    def longestZigZag(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0  
        self.testDFS(root, 0, '')
        return self.ans
        
"""You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0"""