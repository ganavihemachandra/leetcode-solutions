class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        s = list(s)
        start = 0
        end = n - 1
        vowels = set(['a','e','i','o','u','A','E','O','I','U'])
        while(start < end):
            while( start < end and s[start] not in vowels ):
                start += 1
            while( end > 0 and end > start and s[end] not in vowels):
                end -= 1
            
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)
       
