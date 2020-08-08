## Autocomplete with Tries

### Problem Statement

* Build a `Trie` class that contains root node
* Build a `TrieNode` class that inserts a word to `TrieNode` class or finds words in `Trie` node
* add function `suffixes()` to `TrieNode` that can list all complete word suffixes present in the trie

### Implementation

All operations, namely, insert, find, search, are based on single character match based tree traversal from top (root) to down.

### Efficiency

* Time complexity is O(n), since for insert or find operations potentially entire tree has to be traversed and previous characters need to be stored temporarily
* Space complexity is O(1)