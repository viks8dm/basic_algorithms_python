## HTTPRouter using a Trie

### Problem Statement

Implement HTTP router using a Trie.
* A Route class stores routes and their associated handlers
* The Route class uses RouterTrie class for holding routes
* Each node of RouterTrie is definied by a RouterTrieNode class which stores it's children in a dictionary

### Implementation

All operations use simple tree-traversal approach.

### Efficiency

Time efficiency is O(n) at most since a find operation traverses through the entire data-set.
