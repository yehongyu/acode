#coding=utf-8

class Node(object):
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.nodes = {}

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for ch in word:
            if ch not in cur.nodes:
                cur.nodes[ch] = Node(ch)
            cur = cur.nodes[ch]
        cur.is_end = True

    def search_helper(self, root, word):
        if len(word) == 0:
            return root.is_end
        ch = word[0]
        cur = root
        print(word, ch, root.val, root.is_end, len(cur.nodes))
        if len(word) == 1:
            if ch == '.':
                res = False
                for key in cur.nodes.keys():
                    print(key, cur.nodes[key].is_end)
                    res |= cur.nodes[key].is_end
                return res
            else:
                return (ch in cur.nodes) and cur.nodes[ch].is_end
        if ch != '.':
            if ch not in cur.nodes:
                return False
            else:
                return self.search_helper(cur.nodes[ch], word[1:])
        else:
            res = False
            for key in cur.nodes.keys():
                res |= self.search_helper(cur.nodes[key], word[1:])
            return res

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
'''
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
obj.addWord('a')
#print(obj.search('a'))
#print(obj.search('.at'))
obj.addWord('bat')
#print(obj.search('.at'))
#print(obj.search('an.'))
#print(obj.search('a.d.'))
print(obj.search('b.'))
print(obj.search('a.d'))
print(obj.search('.'))
obj.addWord('a')
obj.addWord('a')
print(obj.search('.'))
print(obj.search('a'))
print(obj.search('aa'))
print(obj.search('a'))
print(obj.search('.a'))
print(obj.search('a.'))
'''
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
#print(obj.search('pad'))
#print(obj.search('bad'))
#print(obj.search('.ad'))
print(obj.search('b..'))
