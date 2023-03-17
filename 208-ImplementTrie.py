"""
TrieNode class: This class represents a node in the trie. It has two attributes: children, which is a dictionary that maps characters to child nodes, and is_end, which indicates whether the node represents the end of a word.

Trie class: This class represents the trie itself. It has one attribute: root, which is an instance of TrieNode.

insert method: This method takes a word as input and adds it to the trie. It does this by iterating over each character in the word and creating new nodes if necessary. The time complexity of this method is O(m), where m is the length of the word.

search method: This method takes a word as input and checks if it exists in the trie. It does this by iterating over each character in the word and checking if it exists in its respective node. If all characters are found and the last node has its is_end attribute set to True, then the word exists in the trie. The time complexity of this method is also O(m).

startsWith method: This method takes a prefix as input and checks if any words in the trie start with that prefix. It does this by iterating over each character in the prefix and checking if it exists in its respective node. If all characters are found, then there exists at least one word in the trie that starts with that prefix. The time complexity of this method is also O(m).

The overall space complexity of this code depends on how many words are inserted into the trie and how long they are. In general, tries can have high space complexity because each node can have up to 26 children (for lowercase English letters). However, this can be reduced by using compressed tries or radix trees.
"""

class TrieNode:
    def __init__(self):
        # Initializes an empty dictionary to store the children 
        self.children = {}

        # Initializes a boolean flag to indicate if this node 
        # represents the end of a word
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root 
        for char in word: # Iterates over each character in the word
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        
        node.is_end = True 
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
        
            node = node.children[char]
        
        return True

        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)