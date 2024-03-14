class Solution:
    def guessNumber(self, n: int) -> int:

        begin=1
        end=n
        middle=(begin+end)//2
        while end>=begin:
            if guess(middle)==0: 
                return middle
            if guess(middle)==-1: 
                end=middle-1
                middle=(begin+end)//2
            if guess(middle)==1:
                begin=middle+1
                middle=(begin+end)//2
        
        return middle
        
"""We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

"""