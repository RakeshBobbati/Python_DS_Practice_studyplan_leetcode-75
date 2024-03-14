class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        left,right = 0,0
        max_len =0 
        k =1
        for right in range(length):
            if nums[right]==0:
                k-=1
            while left<right and k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            if k>=0:
                max_len = max(max_len,right-left)
        return max_len

"""Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 """