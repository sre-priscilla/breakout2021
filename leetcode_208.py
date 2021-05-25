# class Trie:

#     def __init__(self):
#         self.root = dict()


#     def insert(self, word: str) -> None:
#         curr = self.root
#         for ch in word:
#             curr = curr.setdefault(ch, dict())
#         curr['#'] = None


#     def search(self, word: str) -> bool:
#         curr = self.root
#         for ch in word:
#             if ch not in curr:
#                 return False
#             curr = curr[ch]
#         return '#' in curr


#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         curr = self.root
#         for ch in prefix:
#             if ch not in curr:
#                 return False
#             curr = curr[ch]
#         return True

class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = [None] * 26
    
    def to_map(self):
        return ''.join([' ' if self.children[i] is None else chr(i + 97) for i in range(26)])

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for ch in word:
            index = ord(ch) - 97
            if root.children[index] is None:
                root.children[index] = TrieNode()
            root = root.children[index]
        root.is_word = True

    def search(self, word):
        root = self.root
        for ch in word:
            index = ord(ch) - 97
            # print(root.to_map())
            if root.children[index] is None:
                return False
            root = root.children[ord(ch) - 97]
        return root.is_word

    def startsWith(self, prefix):
        root = self.root
        for ch in prefix:
            index = ord(ch) - 97
            if root.children[index] is None:
                return False
            root = root.children[ord(ch) - 97]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
# print(obj.startsWith('app'))
# obj.insert('apple')
# print(obj.search('app'))