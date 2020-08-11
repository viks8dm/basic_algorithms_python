## HTTPRouter using a Trie

### Problem Statement

Implement HTTP router using a Trie.
* A Route class stores routes and their associated handlers
* The Route class uses RouterTrie class for holding routes
* Each node of RouterTrie is definied by a RouterTrieNode class which stores it's children in a dictionary

### Implementation

* All operations use simple tree-traversal approach.
* Search, insert, split & lookup operations use Trie data structure

### Efficiency

* Time complexity is O(n), since in worst case senario, search and insert operations take time equal to length of url being searched for.

* Space complexity is also O(n), since full length of path to be search for will have to be traversed.
