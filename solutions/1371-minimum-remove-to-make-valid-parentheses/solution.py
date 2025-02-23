class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []

        for char in s:
            if char =='(':
                res.append(char)
                count += 1
            elif char == ')' and count > 0:
                res.append(char)
                count -= 1
            elif char != ')':
                res.append(char)
        
        filtered = []
        for i in res[::-1]:
            if i == '(' and count > 0:
                count -= 1
            else:
                filtered.append(i)
        return ''.join(filtered[::-1])

# TC: O(N)
# SC: O(N)
