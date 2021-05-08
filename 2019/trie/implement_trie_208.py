#coding=utf-8

class Node(object):
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.nodes = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for ch in word:
            if ch not in cur.nodes:
                cur.nodes[ch] = Node(ch)
            cur = cur.nodes[ch]
        cur.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            if ch in cur.nodes:
                cur = cur.nodes[ch]
            else:
                return False
        return cur.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            if ch in cur.nodes:
                cur = cur.nodes[ch]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.startsWith('app'))
print(obj.search('app'))



