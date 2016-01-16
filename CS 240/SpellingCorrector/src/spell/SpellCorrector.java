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
      // make sure fileName ends to '.txt'
      if (dictionaryFileName.endsWith(".txt")) {
        // import the file
        File dictionary = new File(dictionaryFileName);
        Scanner scanner = new Scanner(dictionary);
        // foreach word in file
        while (scanner.hasNext()) {
          String token = scanner.next();
          // add word to Trie
          trie.add(token);
        }

        scanner.close();
      }

    } catch (Exception e) {
      System.out.println("Exception => " + e);
    }

  }

  public String suggestSimilarWord(String inputWord) throws NoSimilarWordFoundException {
    System.out.println("suggesting a word similar to => " + inputWord);
    return "empty string";
  }

}
