import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.fail;
import org.junit.Test;

import java.io.File;

import hangman.EvilHangmanGame;
import hangman.IEvilHangmanGame.GuessAlreadyMadeException;

public class EvilHangmanTest {
  @Test
  public void createSetTest() {
    EvilHangmanGame test = new EvilHangmanGame();
    File dictionary = new File("words/small.txt");
    int wordLength = 4;
    test.startGame(dictionary, wordLength);
    assertEquals(test.words.size(), 1);
  }
  @Test
  public void filterWordsTest() {
    EvilHangmanGame test = new EvilHangmanGame();
    File dictionary = new File("words/badWords.txt");
    int wordLength = 4;
    test.startGame(dictionary, wordLength);
    assertEquals(test.words.size(), 0);
  }

  // compareTo tests
  @Test
  public void compareToTest() {
    String one = "a--";
    String two = "-a-";
    int result = one.compareTo(two);
    if (result < 0) {
      // System.out.println(one + " is less than " + two);
    } else if (result > 0) {
      // System.out.println(one + " is greater than " + two);
    }
  }
  @Test
  public void getOccurancesTest() {
    EvilHangmanGame game = new EvilHangmanGame();

    String str = "happy";
    char guess = 'p';
    int result = game.getOccurences(str, guess);
    assertEquals(result, 2);
  }

  @Test
  public void createSetTestLarge() {
    EvilHangmanGame test = new EvilHangmanGame();
    File dictionary = new File("words/dictionary.txt");
    int wordLength = 4;
    test.startGame(dictionary, wordLength);
    // System.out.println(test.words.size());
    // assertEquals(test.words.size(), 1);
  }

  @Test
  public void partitionTest() {
    try {
      EvilHangmanGame game = new EvilHangmanGame();
      File dictionary = new File("words/ally.txt");
      int wordLength = 4;
      game.startGame(dictionary, wordLength);
      game.makeGuess('E');
      System.out.println(game.words.toString());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }



}
