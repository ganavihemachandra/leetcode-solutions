class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word
        return dfs(0, self.root)
        
# Time Complexity: 
        # Worst case: O(n * c^n) where n is the length of the word and c is the number of children per node.
        # This happens when the word contains '.' characters, and we need to explore all possible branches.
        # Best case: O(n) when there are no '.' characters, and we just follow the Trie path.

        # Space Complexity:
        # O(n) where n is the length of the word being searched.
        # This is the maximum depth of the recursive call stack in DFS, which can go up to the length of the word.

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
