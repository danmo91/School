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
    System.out.println(test.words.toString());
    assertEquals(test.words.size(), 1);
  }
  @Test
  public void filterWordsTest() {
    EvilHangmanGame test = new EvilHangmanGame();
    File dictionary = new File("words/badWords.txt");
    int wordLength = 4;
    test.startGame(dictionary, wordLength);
    System.out.println(test.words.toString());
    assertEquals(test.words.size(), 0);
  }
}
