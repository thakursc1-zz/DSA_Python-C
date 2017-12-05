class TN:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.endnode = False

class Trie(object):

    def __init__(self):
        self.root = TN(None)
        """
        Initialize your data structure here.
        """
        

    def insert(self, word):
        temp = self.root
        for i in word:
            if i not in temp.children:
                temp.children[i] = TN(i)
                temp = temp.children[i]
            else:
                temp = temp.children[i]
        temp.endnode = True
        return 
            
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for i in word:
            if i not in temp.children:
                return False
            else:
                temp = temp.children[i]
        return temp.endnode==True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        temp = self.root
        for i in prefix:
            if i not in temp.children:
                return False
            else:
                temp = temp.children[i]
        return True 
    
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)