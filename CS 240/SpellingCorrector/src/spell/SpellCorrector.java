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
    transformWord_delete(bestNode, bestWord, inputWord);

    // if null then
      // apply different transformations until i find the best match
      // Delete, transposition, alteration, insertion
      // because i get the node back, i can read the value from it
      // to determine the frequency

    return bestWord.toString();
  }

  public void selectBestWord(StringBuilder bestWord, String transformedWord, TrieNode bestNode, TrieNode resultNode) {
    if (resultNode != null) {
      // compare Node values
      if (resultNode.getValue() > bestNode.getValue()) {
        bestNode = resultNode;
        setBestWord(bestWord, transformedWord);
      } else if (resultNode.getValue() == bestNode.getValue()) {
        // favor alpha order
        if (transformedWord.compareTo(bestWord.toString()) > 0) {
          bestNode = resultNode;
          setBestWord(bestWord, transformedWord);
        }
      }
    }
  }

  public void setBestWord(StringBuilder bestWord, String transformedWord) {
    bestWord.setLength(0); // clear StringBuilder
    bestWord.append(transformedWord);
  }

  public void transformWord_delete(TrieNode bestNode, StringBuilder bestWord, String inputWord) {
    for (int i = 0; i < inputWord.length(); i++) {
      StringBuilder inputWordBuilder = new StringBuilder(inputWord);
      String transformedWord = inputWordBuilder.deleteCharAt(i).toString();
      TrieNode resultNode = trie.find(transformedWord);
      selectBestWord(bestWord, transformedWord, bestNode, resultNode);
    }
  }

}
