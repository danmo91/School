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
  public void startGameTest() {
    EvilHangmanGame test = new EvilHangmanGame();
    File dictionary = new File("dictionary.txt");
    int wordLength = 4;
    test.startGame(dictionary, wordLength);
  }
}
