       
########################
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.end_of_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for 
        # all complete words below this point
        suff_list = []

        if (len(self.children) == 0):
            return suff_list

        for char in self.children:
            if self.children[char].end_of_word:
                suff_list.append(suffix + char)
        
            suff_list += self.children[char].suffixes(suffix + char)
        
        return suff_list

########################
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.end_of_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for c in prefix:
            if c not in node.children:
                # return None
                return TrieNode()
            else:
                node = node.children[c]
        
        return node

########################
if __name__=="__main__":
    MyTrie = Trie()
    wordList = [ "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"]
    for word in wordList:
        MyTrie.insert(word)

    # test - 1
    print("---------- test - 1")
    prefixNode = MyTrie.find("f")
    print("Pass" if prefixNode.suffixes()==['actory', 'un', 'unction'] else "FAIL")

    # test - 2:
    print("---------- test - 2")
    prefixNode = MyTrie.find("a")
    print("Pass" if prefixNode.suffixes()==['nt', 'ntagonist', 'nthology', 'ntonym'] else "FAIL")

    # test - 3:
    print("---------- test - 3")
    prefixNode = MyTrie.find("ant")
    print("Pass" if prefixNode.suffixes()==['agonist', 'hology', 'onym'] else "FAIL")

    # test - 4:
    print("---------- test - 4")
    prefixNode = MyTrie.find("")
    print("Pass" if prefixNode.suffixes()==['ant', 'antagonist', 'anthology', 'antonym', 'tripod', 'trie', 'trigonometry', 'trigger', 'factory', 'fun', 'function'] else "FAIL")

    # test - 5:
    print("---------- test - 5")
    prefixNode = MyTrie.find("trie")
    print("Pass" if prefixNode.suffixes()==[] else "FAIL")

    # test - 6:
    print("---------- test - 6")
    prefixNode = MyTrie.find("fun")
    print("Pass" if prefixNode.suffixes()==['ction'] else "FAIL")

    print("---------- test - 7")
    prefixNode = MyTrie.find("abcd")
    print("Pass" if prefixNode.suffixes()==[] else "FAIL")
