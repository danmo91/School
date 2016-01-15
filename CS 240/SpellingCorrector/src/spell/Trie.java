package spell;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Trie implements ITrie {

  // increase these values when i add a word to the trie
  public int wordCount, nodeCount;
  public TrieNode root;
  Pattern ALPHA;

  public Trie() {
    this.wordCount = 0;
    this.nodeCount = 0;
    this.root = new TrieNode();
    this.ALPHA = Pattern.compile("[a-zA-Z]+");
  }

  public boolean match (String word) {
    Matcher match = this.ALPHA.matcher(word);
    return match.matches();
  }

  public void add(String word) {
    // make sure word contains alphabetic characters
    boolean isWord = this.match(word);

    if (isWord) {
      // move word to StringBuilder object
      StringBuilder wordPartial = new StringBuilder(word);
      // add to root node
      addHelper(root, wordPartial);
    } else
      return;
  }

  void addHelper(TrieNode node, StringBuilder word) {
    // check if node is null
    if (node == null)
      return;
    // check if string is empty
    if (word.length() == 0) {
      // increase node value count
      node.value++;
      // increase wordCount
      this.wordCount++;
      return;
    }

    // get first char of string
    char firstLetter = word.charAt(0);

    // get index based on ascii value of char
    int index = ((int)firstLetter - (int)'a');

    // check if node exists
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

  public TrieNode find(String word) {
    System.out.println("finding word => " + word);
    return new TrieNode();
  }

  public int getWordCount() {
    return wordCount;

  }

  public int getNodeCount() {
    return nodeCount;
  }

  public boolean equals(Trie t) {
    return false;
  }

  // WordNode class has a value and a letter
  public class TrieNode implements ITrie.INode {

    public int value = 0;
    public TrieNode[] childNodes = new TrieNode[26];

    public int getValue() {
      return this.value;
    }

  }

}
