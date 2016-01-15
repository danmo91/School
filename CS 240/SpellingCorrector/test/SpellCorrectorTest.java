

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class SpellCorrectorTest {
  @Test
  public void useDictionary() {
    SpellCorrector spellCorrector = new SpellCorrector();
    spellCorrector.useDictionary("small.txt");

    // initialize smallTrie with expected values
    Trie smallTrie = new Trie();
    assertTrue(spellCorrector.trie.equals(smallTrie));
  }
}
