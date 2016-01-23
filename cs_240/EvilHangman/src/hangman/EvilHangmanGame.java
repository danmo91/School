package hangman;

import java.io.File;
import java.util.Set;
import java.util.TreeSet;
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
    this.lettersGuessed = new TreeSet<String>();
    this.word = new String();
    this.ALPHA = Pattern.compile("[a-zA-Z]+");
  }

  public boolean isWord(String word) {
    Matcher match = this.ALPHA.matcher(word);
    return match.matches();
  }

  public String getWord() {
    return this.word;
  }

  public String getUsedLetters() {
    // return string of lettersGuessed in alphabetical order
    StringBuilder usedLetters = new StringBuilder();
    for (String letter : this.lettersGuessed) {
      usedLetters.append(letter);
      usedLetters.append(" ");
    }
    return usedLetters.toString();
  }

  public void initializeWord(int wordLength) {
    StringBuilder str = new StringBuilder();
    for (int i = 0; i < wordLength; i++) {
      str.append("-");
    }
    this.word = str.toString();
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
    Scanner scanner = null;
    try {
      scanner = new Scanner(dictionary);
      while(scanner.hasNext()) {
        String word = scanner.next().toLowerCase(); // set to lowerCase
        if (word.length() == wordLength && isWord(word)) // check for [a-zA-Z]
          words.add(word);
      }
      initializeWord(wordLength);
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      scanner.close();
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
    if (this.lettersGuessed.contains(String.valueOf(guess))) throw new GuessAlreadyMadeException();

    // add guess to set
    this.lettersGuessed.add(String.valueOf(guess));

    // partition set

    // return largest result set

    Set<String> stub = null;
    return stub;
  }
}
