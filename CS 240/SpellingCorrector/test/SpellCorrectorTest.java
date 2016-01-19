import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;

import spell.SpellCorrector;
import spell.Trie;
import spell.TrieNode;

public class SpellCorrectorTest {

  // Trie.add() tests
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

  // Trie.match() tests
  @Test
  public void wordWithDigits() {
    Trie testTrie = new Trie();
    assertFalse(testTrie.match("dan1"));
  }

  // Trie.getWordCount() tests
  @Test
  public void testWordCount() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    assertEquals(testTrie.getWordCount(), 1);
  }
  @Test
  public void testWordCount2() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("andy");
    assertEquals(testTrie.getWordCount(), 2);
  }
  @Test
  public void testWordCount3() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("dan");
    assertEquals(testTrie.getWordCount(), 1); // returns number of unique words
  }
  @Test
  public void testWordCount4() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("dan1");
    assertEquals(testTrie.getWordCount(), 1); // skips bad words
  }

  // Trie.getNodeCount() tests
  @Test
  public void testNodeCount() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    assertEquals(testTrie.getNodeCount(), 3);
  }
  @Test
  public void testNodeCount2() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("danny");
    assertEquals(testTrie.getNodeCount(), 5);
  }
  @Test
  public void testNodeCount3() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("andy");
    assertEquals(testTrie.getNodeCount(), 7);
  }
  @Test
  public void testNodeCount4() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("dan1");
    assertEquals(testTrie.getNodeCount(), 3);
  }

  // adding char test
  @Test
  public void addingCharTest () {
    char addLetter = (char)(2 + (int)'a');
    assertEquals(addLetter, 'c');
  }

  // Trie.toString() tests
  @Test
  public void toStringTest() {
    Trie testTrie = new Trie();
    testTrie.add("andy");
    String expectedString = "andy\n";
    String actualString = testTrie.toString();
    assertTrue(actualString.equals(expectedString));
  }
  @Test // toString prints in alphabetical order
  public void toStringTest2() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("andy");
    String expectedString = "andy\ndan\n";
    String actualString = testTrie.toString();
    assertTrue(actualString.equals(expectedString));
  }
  @Test // toString prints in alphabetical order
  public void toStringTest3() {
    Trie testTrie = new Trie();
    testTrie.add("dan");
    testTrie.add("andy");
    testTrie.add("cat");
    String expectedString = "andy\ncat\ndan\n";
    String actualString = testTrie.toString();
    assertTrue(actualString.equals(expectedString));
  }

  // TrieNode.equals() tests
  @Test
  public void trieNodeEqualsTest() {
    Trie test = new Trie();
    test.add("a");

    assertTrue(test.equals(test));
  }
  @Test
  public void trieNodeEqualsTest2() {
    Trie test = new Trie();
    test.add("a");

    Trie expect = new Trie();
    expect.add("b");

    assertFalse(test.equals(expect));
  }
  @Test
  public void trieNodeEqualsTest3() {
    Trie test = new Trie();
    test.add("dan");
    test.add("andy");
    test.add("driving");
    test.add("burger");

    assertTrue(test.equals(test));
  }
  @Test
  public void trieNodeEqualsTest4() {
    Trie test = new Trie();
    test.add("dan");
    test.add("andy");

    Trie expect = new Trie();
    expect.add("dann");
    expect.add("andy");

    assertFalse(test.equals(expect));
  }
  @Test
  public void trieNodeEqualsTest5() {
    Trie test = new Trie();
    test.add("DAN");
    test.add("ANDY");
    test.add("DONUT");
    test.add("ZEEBRA");

    Trie expect = new Trie();
    expect.add("dan");
    expect.add("andy");
    expect.add("donut");
    expect.add("zeebra");

    assertTrue(test.equals(expect));
  }
  @Test
  public void trieNodeEqualsTest6() {
    Trie test = new Trie();
    test.add("dan");
    test.add("dan");
    test.add("andy");
    test.add("donut");
    test.add("zeebra");

    Trie expect = new Trie();
    expect.add("dan");
    expect.add("andy");
    expect.add("donut");
    expect.add("zeebra");

    assertFalse(test.equals(expect));
  }

  @Test
  public void trieEqualsTest() {

    try {
      SpellCorrector test = new SpellCorrector();
      test.useDictionary("words/valueTest.txt");

      SpellCorrector test2 = new SpellCorrector();
      test.useDictionary("words/valueTest2.txt");

      assertFalse(test.trie.equals(test2.trie));
    } catch (Exception e) {
      System.out.println("exception in trieEqualsTest => " + e);
    }
  }

  // Trie.find() tests
  @Test
  public void findTest() {
    Trie actual = new Trie();
    actual.add("dan");

    assertTrue(actual.find("dan") != null);
  }
  @Test
  public void findTest2() {
    Trie actual = new Trie();
    actual.add("dan");
    actual.add("danny");

    assertTrue(actual.find("dann") == null);
  }
  @Test
  public void findTest3() {
    Trie actual = new Trie();
    actual.add("dan");
    actual.add("andy");
    actual.add("rohit");
    actual.add("genius");

    assertTrue(actual.find("andy") != null);
  }

  // Trie hashCode() tests
  @Test
  public void hashCodeTest () {
    Trie actual = new Trie();
    actual.add("dan");
    int hash = actual.hashCode();

    // hashCode = nodeCount (3) ^ wordCount (1) * largePrime (7919)
    assertEquals(2147483647, actual.hashCode());
  }

  // SpellCorrector useDictionary() tests
  @Test
  public void useDictionaryTest () {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/small.txt";

    try {
      test.useDictionary(dictionaryFileName);
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }

    assertEquals(12, test.trie.getWordCount());
    assertTrue(test.trie.root.equals(test.trie.root));

  }
  @Test
  public void useDictionaryTest2 () {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/med.txt";

    try {
      test.useDictionary(dictionaryFileName);
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }

    assertEquals(64, test.trie.getWordCount());
    assertTrue(test.trie.root.equals(test.trie.root));

  }
  @Test
  public void useDictionaryTest3 () {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/med";

    try {
      test.useDictionary(dictionaryFileName);
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }

    assertEquals(0, test.trie.getWordCount());

  }

  @Test
  public void useDictionaryTest4 () {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/words.txt";
    String dictionaryFileName2 = "words/words2.txt";

    SpellCorrector expected = new SpellCorrector();

    try {
      test.useDictionary(dictionaryFileName);
      expected.useDictionary(dictionaryFileName2);
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }
    assertFalse(test.trie.root.equals(expected.trie.root));
  }

  // suggestSimilarWord Tests
  @Test
  public void suggestSimilarWordTest() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/small.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("ANDY");
      assertTrue(similarWord.equals("andy"));
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }
  }
  @Test
  public void transformWord_deleteTest() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/small.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("anddy");
      assertTrue(similarWord.equals("andy"));
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }
  }

  @Test // favor words with greater value
  public void transformWord_deleteTest2() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/small.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("cool");
      assertTrue(similarWord.equals("col"));
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }
  }

  @Test // favor words in alphabetical order
  public void transformWord_deleteTest3() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/deleteTest.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("bird");
      assertTrue(similarWord.equals("bid"));
    } catch (Exception e) {
      System.out.println("Exception in test => " + e);
    }
  }

  @Test // transposition test
  public void transformWord_transposeTest() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/transposeTest.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("house");
      assertTrue(similarWord.equals("hosue"));
    } catch (Exception e) {
      System.out.println("Exception in transformWord_transposeTest => " + e);
    }
  }

  @Test // alteration test
  public void transformWord_alterateTest() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/alterateTest.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("bob");
      assertTrue(similarWord.equals("aob"));
    } catch (Exception e) {
      System.out.println("Exception in transformWord_alterateTest => " + e);
    }
  }

  @Test // alteration test
  public void transformWord_alterateTest2() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/alterateTest2.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("bob");
      assertTrue(similarWord.equals("eob"));
    } catch (Exception e) {
      System.out.println("Exception in transformWord_alterateTest => " + e);
    }
  }

  @Test // alteration test
  public void transformWord_insert() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/insertTest.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("ask");
      assertTrue(similarWord.equals("aask"));
    } catch (Exception e) {
      System.out.println("Exception in transformWord_alterateTest => " + e);
    }
  }

  @Test // alteration test
  public void transformWord_insert2() {
    SpellCorrector test = new SpellCorrector();
    String dictionaryFileName = "words/insertTest2.txt";

    try {
      test.useDictionary(dictionaryFileName);
      String similarWord = test.suggestSimilarWord("ask");
      assertTrue(similarWord.equals("askc"));
    } catch (Exception e) {
      System.out.println("Exception in transformWord_alterateTest => " + e);
    }
  }

}
