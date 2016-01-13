# Spelling Corrector

Google provides a more powerful spell corrector for validating the keywords we type into the input text box. It not only checks against a dictionary, but, if it doesn’t find the keyword in the dictionary, it suggests a most likely replacement.

Our spell checker will only validate a single word rather than each word in a list of words.

## Requirements

-[] Generate a dictionary (Trie) with words.txt

## Compiling and Running the project

``` sh
$ javac src/*.java -d bin/
$ java -cp bin spell.Main [dictionary.txt] [word]
```
