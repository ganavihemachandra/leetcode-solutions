class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1, 0, -1):
            current = one + two
            two = one
            one = current
        return one   

# TC - O(N)
# SC - O(1)
