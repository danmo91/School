package spell;

public class Words implements ITrie {

  public void add(String word) {
    System.out.println("adding a word => " + word);
  }

  public WordNode find(String word) {
    System.out.println("finding word => " + word);
    return new WordNode();
  }

  public int getWordCount() {
    System.out.println("the number of unique words in a trie");
    return -1;

  }

  public int getNodeCount() {
    System.out.println("the number of nodes in a trie");
    return -1;
  }

  // WordNode class has a value and a letter
  public class WordNode implements ITrie.INode {

    int value;
    char letter;

    public int getValue() {
      return this.value;
    }

  }

}
