class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for i in strs:
            anagram_word = ''.join(sorted(i))
            anagramMap[anagram_word].append(i)
        return list(anagramMap.values())

# Time Complexity - O(N * LlogL), L is the length of string
# Space Complexity - O(N*L)
