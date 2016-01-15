package spell;

import java.io.IOException;

public class SpellCorrector implements ISpellCorrector {

  Trie trieOfWords;

  public void useDictionary(String dictionaryFileName) throws IOException {
    System.out.println("use this dictionary => " + dictionaryFileName);
  }

  public String suggestSimilarWord(String inputWord) throws NoSimilarWordFoundException {
    System.out.println("suggesting a word similar to => " + inputWord);
    return "empty string";
  }

}
