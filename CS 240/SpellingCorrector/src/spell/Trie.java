package spell;

public class Trie implements ITrie {

  // increase these values when i add a word to the trie
  int wordCount;
  int nodeCount;

  public void add(String word) {
    System.out.println("adding a word => " + word);
  }

  public TrieNode find(String word) {
    System.out.println("finding word => " + word);
    return new TrieNode();
  }

  public int getWordCount() {
    System.out.println("the number of unique words in a trie");
    return -1;

  }

  public int getNodeCount() {
    System.out.println("the number of nodes in a trie");
    return -1;
  }

  public boolean equals(Trie t) {
    return false;
  }

  // WordNode class has a value and a letter
  public class TrieNode implements ITrie.INode {

    int value;
    // WordNode [26];

    public int getValue() {
      return this.value;
    }

  }

}
