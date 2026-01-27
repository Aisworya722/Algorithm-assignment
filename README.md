# Algorithm Assignment

## Files
- quicksort.py (Randomized Quicksort + Deterministic Quicksort)
- chaining_hash_table.py (Hash Table with Chaining: insert/search/delete)

## How to run
### Quicksort test
1. Open terminal in this folder
2. Run: python
3. Paste:

from quicksort import randomized_quicksort, deterministic_quicksort
print(randomized_quicksort([5,2,9,1,5,6]))
print(deterministic_quicksort([5,2,9,1,5,6]))

### Hash table test
1. Run: python
2. Paste:

from chaining_hash_table import ChainingHashTable
ht = ChainingHashTable()
ht.insert("apple", 10)
print(ht.search("apple"))

