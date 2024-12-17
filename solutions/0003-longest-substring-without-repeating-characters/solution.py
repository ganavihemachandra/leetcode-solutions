class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

# TC - O(N)
# SC - min(O(N, c)), where C is the size of character set and n is the str length
        
