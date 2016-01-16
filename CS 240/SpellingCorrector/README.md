# Spelling Corrector

Google provides a more powerful spell corrector for validating the keywords we type into the input text box. It not only checks against a dictionary, but, if it doesn’t find the keyword in the dictionary, it suggests a most likely replacement.

Our spell checker will only validate a single word rather than each word in a list of words.

## Functionality

- If the word is found, the SpellingCorrector will return the input word in 'lowercase'
- If the word is not found, the SpellingCorrector will return the most similar word, again in 'lowercase'
- If no similar word is found (a word with a Distance < 3) throw a NoSimilarWordFoundException

Similar word criteria:
1. has the "closest" edit distance
2. found the most time in the dictionary
3. if two words have the same edit distance and frequency, favor the first alphabetical answer




## Compiling and Running the project

``` sh
# compile with -g for jdb debugging information
$ javac -g -d bin/ src/spell/*.java
$ java -cp bin/ spell.Main [dictionary.txt] [word]
```

## Debugging with JDB

(http://www.javaworld.com/article/2077445/testing-debugging/debug-with-jdb.html)
include the -sourcepath option to show the source code inline with the debugger

```sh
$ jdb -classpath bin/ -sourcepath src/ spell.Main [dictionary.txt] [word]
# debugging test cases
$ jdb -classpath .:lib/junit-4.12.jar:lib/hamcrest-core-1.3.jar:test/:src/:bin/ org.junit.runner.JUnitCore SpellCorrectorTest
```

### Breakpoints

Examples of setting breakpoints:

```sh
# stop at specific line number
stop at [class]:[line number]
stop at Main:21

# stop at beginning of main method
stop in [package].[class].[method]
stop in spell.Main.main
```

### other commands
- run
- step
- next => step over
- list => show current source code frame
- print => prints object value
- dump => prints whole object
- locals

## JUNIT Testing

(https://github.com/junit-team/junit/wiki/Getting-started)

### Compile and Running tests

```sh
$ javac -cp lib/junit-4.12.jar:hamcrest-core-1.3.jar -sourcepath src/ -d bin/ -g test/SpellCorrectorTest.java

$ java -cp .:lib/junit-4.12.jar:lib/hamcrest-core-1.3.jar:test/:src/:bin/ org.junit.runner.JUnitCore SpellCorrectorTest
```

## Trie class

### ToString()

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
    // check getClass type
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
