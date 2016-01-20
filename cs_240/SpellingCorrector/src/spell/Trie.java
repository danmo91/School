package spell;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

// Tree structure that holds nodes of words
public class Trie implements ITrie {

  public int wordCount, nodeCount;
  public TrieNode root;
  Pattern ALPHA; // REGEX pattern for matching words

  public Trie() {
    this.wordCount = 0;
    this.nodeCount = 1;
    this.root = new TrieNode();
    this.ALPHA = Pattern.compile("[a-zA-Z]+");
  }

  public int getWordCount() {
    return wordCount;
  }

  public int getNodeCount() {
    return nodeCount;
  }

  // adds a word to the Trie structure
  public void add(String word) {
    boolean isWord = this.match(word); // make sure word contains alphabetic characters
    if (isWord) {
      // make word lowercase, convert to StringBuilder
      StringBuilder wordBuilder = new StringBuilder(word.toLowerCase());
      addHelper(root, wordBuilder);
    } else
    return;
  }

  // Helper methods for add()
  void addHelper(TrieNode node, StringBuilder word) {
    if (node == null)
      return;

    // BASE CASE: check if string is empty
    if (word.length() == 0) {
      node.value++;
      if (node.value == 1)
      this.wordCount++;
      return;
    }

    // get first char of string
    char firstLetter = word.charAt(0);

    // get index based on ascii value of char
    int index = ((int)firstLetter - (int)'a');

    // create node if DNE
    if (node.childNodes[index] == null) {
      node.childNodes[index] = new TrieNode();
      this.nodeCount++;
    }

    // childNode
    TrieNode childNode = node.childNodes[index];

    // trim off first letter
    word.deleteCharAt(0);

    // pass to addHelper
    addHelper(childNode, word);

  }

  // returns true if the word matches pattern [a-zA-Z]
  public boolean match (String word) {
    Matcher match = this.ALPHA.matcher(word);
    return match.matches();
  }

  // Searches Trie for matching word, return TrieNode pointer if found, else null
  public TrieNode find(String word) {
    boolean isWord = this.match(word); // make sure word only contains [a-zA-Z]
    TrieNode returnNode = null;
    if (isWord) {
      StringBuilder wordBuilder = new StringBuilder(word.toLowerCase()); // make sure search word is lowercase
      returnNode = findHelper(this.root, wordBuilder, returnNode);
    }
    return returnNode;
  }

  TrieNode findHelper(TrieNode node, StringBuilder word, TrieNode returnNode) {
    // BASE CASE: found word
    if (word.length() == 0) {
      if (node.value > 0) {
        returnNode = node;
        return returnNode;
      } else {
        return null;
      }
    }

    // get first char of string
    char firstLetter = word.charAt(0);

    // get index based on ascii value of char
    int index = ((int)firstLetter - (int)'a');

    // check if node exists
    if (node.childNodes[index] == null) {
      return null;
    }

    // childNode
    TrieNode childNode = node.childNodes[index];

    // trim off first letter
    word.deleteCharAt(0);
    return findHelper(childNode, word, returnNode);

  }

  public boolean equals(Trie t) {
    // check getClass types
    if (!this.getClass().equals(t.getClass())) {
      return false;
    }
    if (t.getWordCount() != this.getWordCount()) {
      return false;
    }
    if (t.getNodeCount() != this.getNodeCount()) {
      return false;
    }

    return this.root.equals(t.root);
  }

  public String toString() {
    StringBuilder word = new StringBuilder();
    StringBuilder output = new StringBuilder();
    toStringHelper(this.root, word, output);
    return output.toString();
  }

  public void toStringHelper(TrieNode node, StringBuilder word, StringBuilder output) {
    if (node == null) {
      return;
    }
    if (node.value > 0) {
      output.append(word.toString() + "\n");
    }
    for (int i = 0; i < 26; i++) {
      char addLetter = (char)(i + (int)'a');
      word.append(addLetter);
      toStringHelper(node.childNodes[i], word, output);
      word.setLength(word.length() - 1);
    }
  }

  @Override
  public int hashCode() {
    int largePrime = 7919;
    int hash = (int)Math.pow(this.nodeCount * this.wordCount, largePrime);

    // to add more entropy check how many of the 26 nodes we have in root

    return hash;
  }

}
