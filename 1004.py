class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left,right = 0,0
        max_len = 0
        for right in range(length):
            if nums[right]==0:
                k-=1
            while left<right and k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            if k>=0:
                max_len = max(max_len,right-left+1) 
        return max_len


"""Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 """