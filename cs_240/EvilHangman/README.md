# Evil Hangman

- The computer tries to make the humans lose (and they almost always do).
- The user supplies the length of the word they want to play with.
- The program chooses the word at the end of the game

## Project Tips

1. Read the dictionary.txt into a set of strings, only keep the ones that match the word length
2. Ask the user for a guess
3. Partition the set into subsets, and pick the largest subset to replace the set
4. the user filters down to a set of one and guesses it correctly, they could win

Set of Strings
map of subsets, 2^n is the max number of partitions
- key = String that represents the pattern
- value = set of Strings

foreach possible pattern
  foreach word in dictionary
    check if word matches pattern
    if match
      add to matching set in map of partitions

```java
public String makePattern(String word, char guess) {
  // return string with guess letter and '-'
}
```
What are the tie breaker rules?

## Java

### Collections
(like C++ containers)
generic interface that all list-like things inherit from.
Maps are not collections because it is a set of {key:value} pairs
Iterator, allows you to enumerate or traverse a collection

#### List
ArrayList (resizable array, faster accessing, more memory)
LinkedList (doubly-linkd list, faster add/remove, less memory)
ListIterator, can move forward/backward

#### Set
a collection of unique values, unordered, (no duplicates)

HashSet (hash table implementation, faster, more memory)
TreeSet (balanced binary search tree, slower, less memory)
LinkedHashSet (hash table + linked list)

#### Map
entrySet returns a set of {key:value}

you need to @Override equals and hashCode together
if you want to use sortable collections, you need to implement comparable to your class (compareTo())
try to use your objects fields.compareTo() methods as much as possible

```java
public int compareTo(Object other) {
  if (this.number < other.number) {
    return -1;
  } else if (this.number > other.number) {
    return 1;
  } else {

  }
}
```
