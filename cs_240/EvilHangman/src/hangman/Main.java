package hangman;

import hangman.IEvilHangmanGame.GuessAlreadyMadeException;
import java.util.Scanner;
import java.io.File;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Main {

  public static void main(String[] args) {
    try {
      // get args
      validateArgs(args);
      File dictionaryFileName = new File(args[0]);
      int wordLength = Integer.valueOf(args[1]);
      int numGuesses = Integer.valueOf(args[2]);

      // Start game
      EvilHangmanGame game = new EvilHangmanGame();
      game.startGame(dictionaryFileName, wordLength);
      if (game.words.size() == 0) throw new Exception("not enough words to play game");
      runGame(numGuesses, game);

    } catch (Exception e) {
      e.printStackTrace();
      System.out.println("USAGE: java -cp bin/ hangman.Main [dictionary.txt] [wordLengh] [guesses]");
    }
  }

  public static boolean validateGuess(String guess) {
    if (guess.length() > 1) return false;
    Pattern ALPHA = Pattern.compile("[a-zA-Z]{1}");
    Matcher match = ALPHA.matcher(guess);
    return match.matches();
  }

  public static void handleGuess(Scanner userInput, EvilHangmanGame game) {
    // Ask the user to make a guess, validate input, make guess
    try {
      boolean isValid = false;
      while (!isValid) {
        System.out.print("Enter guess: ");
        String guess = userInput.next().toLowerCase();
        isValid = validateGuess(guess);
        if (isValid) {
          game.makeGuess(guess.charAt(0));
        } else {
          System.out.println("Invalid input");
        }
      }
    } catch (GuessAlreadyMadeException e) {
      System.out.println("You already used that letter");
      handleGuess(userInput, game);
    }
  }

  public static void runGame(int numGuesses, EvilHangmanGame game) {

    Scanner userInput = new Scanner(System.in);
    try {
      for (int i = numGuesses; i > 0; i--) {
        if (i == 1) System.out.println("\nYou have 1 guess left");
        else System.out.println("You have " + i + " guesses left");
        System.out.print("Used letters: " + game.getUsedLetters());
        System.out.println("\nword: " + game.getWord());
        handleGuess(userInput, game);
      }
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      userInput.close();
    }
  }

  public static void validateArgs(String[] args) {
    if (args.length < 3) throw new IllegalArgumentException("missing required number of arguments");
    if (Integer.valueOf(args[1]) < 2) throw new IllegalArgumentException("word length must be >= 2");
    if (Integer.valueOf(args[2]) < 1) throw new IllegalArgumentException("number of guesses must be >= 1");
  }
}
