import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.fail;
import org.junit.Test;

import spell.SpellCorrector;
import spell.Trie;
import spell.TrieNode;
import spell.ISpellCorrector.NoSimilarWordFoundException;

public class EditDistanceTests {

@Test
public void transformWord_delete() {
  SpellCorrector test = new SpellCorrector();
  String dictionaryFileName = "words/deleteDistanceTwo.txt";
  try {
    test.useDictionary(dictionaryFileName);
    String similarWord = test.suggestSimilarWord("dan");
    // assertTrue(similarWord.equals("a"));
  } catch (Exception e) {
    System.out.println("NoSimilarWordException => " + e);
    fail("failed editDistanceTwo_delete");
  }
}


}
