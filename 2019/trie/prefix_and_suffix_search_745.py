#coding=utf-8

class Node(object):
    def __init__(self, val):
        self.val = val
        self.idx = -1
        self.nodes = {}

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pre_root = Node("")
        self.suff_root = Node("")
        for i in range(len(words)):
            word = words[i]
            reverse_word = []
            for j in range(len(word)-1, -1, -1):
                reverse_word.append(word[j])
            print(i, word, reverse_word)
            self.addWord(self.pre_root, i, word)
            self.addWord(self.suff_root, i, reverse_word)

    def addWord(self, root, i, word):
        cur = root
        for ch in word:
            if ch not in cur.nodes:
                print('add', ch)
                cur.nodes[ch] = Node(ch)
            cur = cur.nodes[ch]
        cur.idx = i

    def f_helper(self, root, prefix, idxs):
        cur = root
        print(prefix, idxs, cur.val, cur.idx)
        if len(prefix) == 0:
            if cur.idx > -1:
                idxs.append(cur.idx)
            for key in cur.nodes:
                if cur.nodes[key].idx > -1:
                    idxs.append(cur.nodes[key].idx)
                self.f_helper(cur.nodes[key], prefix, idxs)
        else:
            if prefix[0] in cur.nodes:
                self.f_helper(cur.nodes[prefix[0]], prefix[1:], idxs)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        pre_idxs = []
        self.f_helper(self.pre_root, prefix, pre_idxs)
        reverse_suffix = []
        for j in range(len(suffix)-1, -1, -1):
            reverse_suffix.append(suffix[j])
        print('prefix:', prefix, suffix, reverse_suffix)
        suff_idxs = []
        self.f_helper(self.suff_root, reverse_suffix, suff_idxs)
        res = -1
        print('res:', pre_idxs)
        print('res:', suff_idxs)
        for idx in pre_idxs:
            if idx in suff_idxs:
                res = max(res, idx)
        return res


# Your WordFilter object will be instantiated and called as such:
obj = WordFilter(['pop'])
print(obj.f('', 'pop'))
'''
obj = WordFilter(['apple'])
print(obj.f('a', 'e'))
print(obj.f('b', ''))
'''
