import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;

import spell.SpellCorrector;
import spell.Trie;
import spell.Trie.TrieNode;

public class SpellCorrectorTest {
  @Test
  public void addWordToTrie() {

    Trie testTrie = new Trie();
    testTrie.add("dan");

    // // build expected trie
    // Trie expectedTrie = new Trie();
    //
    // // add 'dan', increase nodeCount, wordCount
    // expectedTrie.root.childNodes[3].childNodes[0].childNodes[13].value = 1;
    // expectedTrie.nodeCount = 3;
    // expectedTrie.wordCount = 1;
    //
    // // check if equal
    // assertTrue(testTrie.equals(expectedTrie));

  }
  @Test
  public void wordWithDigits() {
    Trie trie = new Trie();
    assertFalse(trie.match("dan1"));
  }
}
