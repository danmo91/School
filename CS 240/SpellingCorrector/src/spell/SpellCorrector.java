package spell;

import java.io.IOException;
import java.util.Scanner;
import java.io.File;

public class SpellCorrector implements ISpellCorrector {

  public Trie trie;

  public SpellCorrector () {
    trie = new Trie();
  }

  public void useDictionary(String dictionaryFileName) throws IOException {
    try {
      File dictionary = new File(dictionaryFileName);
      Scanner scanner = new Scanner(dictionary);
      while (scanner.hasNext()) {
        trie.add(scanner.next());
      }
      scanner.close();
    } catch (Exception e) {
      System.out.println("Exception => " + e);
    }
  }

  public String suggestSimilarWord(String inputWord) throws NoSimilarWordFoundException {

    // first try to find inputWord in Trie
    if (trie.find(inputWord) != null) {
      return inputWord.toLowerCase();
    }

    TrieNode bestNode = new TrieNode(); // should be null? or having getValue() return 0 enough?
    StringBuilder bestWord = new StringBuilder();

    // delete, edit distance 1
    bestNode = transformWord_delete(bestNode, bestWord, inputWord);

    System.out.println("suggested word => " + bestWord.toString());

    return bestWord.toString();
  }

  public TrieNode selectBestWord(StringBuilder bestWord, String transformedWord, TrieNode bestNode, TrieNode resultNode) {
    if (resultNode != null) {
      // compare Node values
      if (resultNode.getValue() > bestNode.getValue()) {
        bestNode = resultNode;
        setBestWord(bestWord, transformedWord);
      } else if (resultNode.getValue() == bestNode.getValue()) {
        // favor alpha order
        if (transformedWord.compareTo(bestWord.toString()) < 0) {
          bestNode = resultNode;
          setBestWord(bestWord, transformedWord);
        }
      }
    }
    return bestNode;
  }

  public void setBestWord(StringBuilder bestWord, String transformedWord) {
    bestWord.setLength(0); // clear StringBuilder
    bestWord.append(transformedWord);
  }

  public TrieNode transformWord_delete(TrieNode bestNode, StringBuilder bestWord, String inputWord) {
    for (int i = 0; i < inputWord.length(); i++) {
      StringBuilder inputWordBuilder = new StringBuilder(inputWord);
      String transformedWord = inputWordBuilder.deleteCharAt(i).toString();
      TrieNode resultNode = trie.find(transformedWord);
      bestNode = selectBestWord(bestWord, transformedWord, bestNode, resultNode);
    }
    return bestNode;
  }

}
