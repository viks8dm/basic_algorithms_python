## Autocomplete with Tries

### Problem Statement

* Build a `Trie` class that contains root node
* Build a `TrieNode` class that inserts a word to `TrieNode` class or finds words in `Trie` node
* add function `suffixes()` to `TrieNode` that can list all complete word suffixes present in the trie

### Implementation

All operations, namely, insert, find, search, are based on single character match via tree traversal from top (root) to down.

### Efficiency

* Worst case time complexity is O(n*m), for insert and find operations, where n is number of words and m is length of a word. This is derived from the corresponding implementations where insert and find operations look at each word in the dictionary and every character in the "word-tree" is traversed.
    * the suffixes() function has order O(k)*O(l), where k is length of all suffices and l is lenght of words, since each character in suffix and each word is compared

* Worst case space complexity for insert operation is O(n) where n is number of words
