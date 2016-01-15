# Spelling Corrector

Google provides a more powerful spell corrector for validating the keywords we type into the input text box. It not only checks against a dictionary, but, if it doesn’t find the keyword in the dictionary, it suggests a most likely replacement.

Our spell checker will only validate a single word rather than each word in a list of words.

## Compiling and Running the project

``` sh
# compile with -g for jdb debugging information
$ javac src/spell/*.java -d bin/ -g
$ java -cp bin/ spell.Main [dictionary.txt] [word]
```

## Debugging
compile with -g option to generate debugging information
include the -sourcepath option to show the source code inline with the debugger

```sh
$ jdb -classpath bin/ -sourcepath src/ spell.Main [dictionary.txt] [word]
```

### Breakpoints
```sh
stop at [class]:[line number]
# stop at beginning of main method
stop in spell.Main.main

stop in [package].[class].[method]
```

### other commands
run
step
print
dump
locals

## Requirements

-[] Generate a dictionary (Trie) with words.txt

### Implement Trie class

#### ToString()

```java
class Trie {

  TrieNode root;

  // prints out the value of trie
  public String toString() {
    StringBuilder word = new StringBuilder()
    StringBuilder output = new StringBuilder()
    toStringHelper(root, word, output);
    return output.toString();
  }

  private void toStringHelper(TrieNode n, StringBuilder word, StringBuilder output) {

    if (n == null) {
      return;
    }

    if (n.getValue() > 0) {
      // add word to output list of words
      output.append(word.toString() + "\n");
    }

    // for each child, call toString()
    for (int i = 0; i < 26; i++) {
      word.append(i + 'a'); // make sure this is a char (i + 'a') == ascii value for char
      toStringHelper(n.getChild(i), word, output);
      word.setLength(word.getLength() - 1);
    }

  }

  @Override
  public bool equals(Trie t) {
    // check classType
    // check for null

    // check word count
    // check node count

    // for each node (add an equals method on the Node class)
      // check count
      // check array

  }

  // quickly and consistently returns a unique integer
  // if two Tries are equal, they are should return the same hashCode
  @Override
  public int hashCode() {
    // use nodeCount and wordCount to generate a consistent number
    // bit-shift, multiply, prime numbers
  }

}
```
