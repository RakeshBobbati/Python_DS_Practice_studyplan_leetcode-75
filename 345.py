class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i,j = 0,len(s)-1
        vowels = set('aeiou')
        while i<j:
            if s[i].lower() not in vowels:
                i+=1
            elif s[j].lower() not in vowels:
                j-=1

            else:
                s[i],s[j] = s[j],s[i]
                j-=1
                i+=1
        return "".join(s)

"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

"""