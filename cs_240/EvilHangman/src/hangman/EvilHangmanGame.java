package hangman;

import java.io.File;
import java.util.Set;
import java.util.HashSet;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class EvilHangmanGame implements IEvilHangmanGame {

  public Set<String> words;
  public Set<String> lettersGuessed;
  public String word;
  Pattern ALPHA;

  public EvilHangmanGame() {
    this.words = new HashSet<String>();
    this.lettersGuessed = new HashSet<String>();
    this.word = new String();
    this.ALPHA = Pattern.compile("[a-zA-Z]+");
  }

  public boolean isWord(String word) {
    Matcher match = this.ALPHA.matcher(word);
    return match.matches();
  }


  /**
   * Starts a new game of evil hangman using words from <code>dictionary</code>
   * with length <code>wordLength</code>.
   *	<p>
   *	This method should set up everything required to play the game,
   *	but should not actually play the game. (ie. There should not be
   *	a loop to prompt for input from the user.)
   *
   * @param dictionary Dictionary of words to use for the game
   * @param wordLength Number of characters in the word to guess
   */
  public void startGame(File dictionary, int wordLength) {
    // load words
    try {
      Scanner scanner = new Scanner(dictionary);
      while(scanner.hasNext()) {
        String word = scanner.next().toLowerCase(); // set to lowerCase
        if (word.length() == wordLength && isWord(word)) // check for [a-zA-Z]
          words.add(word);
      }
      scanner.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }


  /**
   * Make a guess in the current game.
   *
   * @param guess The character being guessed
   *
   * @return The set of strings that satisfy all the guesses made so far
   * in the game, including the guess made in this call. The game could claim
   * that any of these words had been the secret word for the whole game.
   *
   * @throws GuessAlreadyMadeException If the character <code>guess</code>
   * has already been guessed in this game.
   */
  public Set<String> makeGuess(char guess) throws GuessAlreadyMadeException {
    System.out.println("makeGuess");
    Set<String> stub = null;
    return stub;
  }
}
