echo '> Testing SpellingCorrector 🙌🏼\n>'

java -cp bin spell.Main words/words.txt dan

# testing with no file, word
java -cp bin/ spell.Main
# test with no word
java -cp bin/ spell.Main words/small.txt

echo '> \n> End Test.🍕\n'
