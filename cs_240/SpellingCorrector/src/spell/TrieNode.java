package spell;

/**
 * TrieNode class implements the ITrie.INode interface
 */
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
