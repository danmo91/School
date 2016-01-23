package hangman;

import hangman.IEvilHangmanGame.GuessAlreadyMadeException;
import java.util.Scanner;
import java.io.File;

public class Main {

  public static void runGame(int numGuesses, EvilHangmanGame game) {

    Scanner userInput = new Scanner(System.in);

    for (int i = 0; i < numGuesses; i++) {

      // Display the number of remaining guesses, list of letters guessed, and partially constructed word
      if (numGuesses - i == 1) {
        System.out.println("You have 1 guess left");
      } else {
        System.out.println("You have " + (numGuesses - i) + " guesses left");
      }

      System.out.print("Used letters: ");
      for (String letter : game.lettersGuessed) {
        System.out.print(letter + " ");
      }
      
      System.out.println("\nword: [---a-]");

      // Ask the user to make a guess
      System.out.print("Enter guess: ");
      String guess = userInput.next();

      // makeGuess(), validate input

      // report the number of positions the letter appears
      System.out.println("");

    }

    userInput.close();

    // pick a word from the list
    // compareTo user's guess
    // report result

  }

  public static void main(String[] args) {
    try {

      // validate args
      if (args.length < 3) throw new IllegalArgumentException("missing required number of arguments");
      if (Integer.valueOf(args[1]) < 2) throw new IllegalArgumentException("word length must be >= 2");
      if (Integer.valueOf(args[2]) < 1) throw new IllegalArgumentException("number of guesses must be >= 1");

      // get args
      File dictionaryFileName = new File(args[0]);
      int wordLength = Integer.valueOf(args[1]);
      int numGuesses = Integer.valueOf(args[2]);

      // Start game
      EvilHangmanGame game = new EvilHangmanGame();
      game.startGame(dictionaryFileName, wordLength);
      runGame(numGuesses, game);

    } catch (Exception e) {
      e.printStackTrace();
      System.out.println("USAGE: java -cp bin/ hangman.Main [dictionary.txt] [wordLengh] [guesses]");
    }
  }
}
