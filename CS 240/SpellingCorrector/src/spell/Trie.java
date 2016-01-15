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
      StringBuilder wordBuilder = new StringBuilder(word);
      // add to root node
      addHelper(root, wordBuilder);
    } else
      return;
  }

  void addHelper(TrieNode node, StringBuilder word) {
    // check if node is null
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
    // check getClass() type
    if (!this.getClass().equals(t.getClass())) {
      return false;
    }

    if (t == null) {
      return false;
    }

    if (t.getWordCount() != this.getWordCount()) {
      return false;
    }

    if (t.getNodeCount() != this.getNodeCount()) {
      return false;
    }

    if (this.root.equals(t.root)) {
      return true;
    }

    return false;
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

  // WordNode class has a value and a letter
  public class TrieNode implements ITrie.INode {

    public int value;
    public TrieNode[] childNodes;

    public TrieNode() {
      this.value = 0;
      childNodes = new TrieNode[26];
    }

    public int getValue() {
      return this.value;
    }

    public boolean equals(TrieNode node) {
      Boolean result = true;
      if (this.value != node.value) {
        result = false;
      }
      for (int i = 0; i < 26 && result; i++) {
        if (this.childNodes[i] == null && node.childNodes[i] == null) {
          // skip
        } else if (this.childNodes[i] == null || node.childNodes[i] == null) {
          result = false;
        } else {
          result = this.childNodes[i].equals(node.childNodes[i]);
        }
      }
      return result;
    }

  }

}
