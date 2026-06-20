class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for index in range(j, len(word)):
                if word[index] == '.':
                    #check all children + continue to the next letter
                    for child in curr.children.values():
                        if dfs(index + 1, child):
                            return True
                    return False
                elif word[index] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[index]]
            return curr.end
        return dfs(0, self.root)
