class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i=0
        while i<len(asteroids):
            if len(stack)==0: 
                stack.append(asteroids[i])    
            #If asteroids on top of stack is moving right and current asteroids is moving left they will collide
            elif stack[-1]>0 and asteroids[i]<0:
                val=0
            #If the asteroid[i] is bigger then asteroids on top of stack it will keep destroying them until the condition dissatifies
                while len(stack)!=0 and stack[-1]<=abs(asteroids[i]) and stack[-1]>0:
                    val=stack.pop()
                    #If both the asteroid and asteroids on top of stack have same mass, they will destroy each other and the loop should break
                    if val==abs(asteroids[i]): 
                        break
            #If the len of stack is not zero and top is stack is also moving to left then asteroid[i] will also be appended as it is also moving left and would not collied with stack top
                if len(stack)!=0 and stack[-1]<0 and abs(val)!=abs(asteroids[i]):
                    stack.append(asteroids[i])
            #If the asteroids[i] has destroyed all asteroids in the stack
                if len(stack)==0 and abs(val)!=abs(asteroids[i]):
                    stack.append(asteroids[i])
            else:
                stack.append(asteroids[i])
            i+=1
        return stack


"""We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 """