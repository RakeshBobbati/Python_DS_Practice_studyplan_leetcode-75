class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = [False]*n
        province = 0
        def DFS(city):
            for i in range(len(city)):
                if city[i]==1 and not seen[i]:
                    seen[i] = True
                    DFS(isConnected[i])
        for i in range(n):
            if not seen[i]:
                seen[i]=True
                DFS(isConnected[i])
                province+=1
        return province
            
"""There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3"""