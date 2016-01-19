echo '> Testing SpellingCorrector 🙌🏼\n'


echo '> Normal: dictionary => words.txt, word => dan'
java -cp bin spell.Main words/words.txt dan

echo '\n> Missing arguments test 1'
# testing with no file, word
java -cp bin/ spell.Main

echo '\n> Missing arguments test 2'
# test with no word
java -cp bin/ spell.Main words/small.txt

echo '\n> Single letter word test'
# test with no word
java -cp bin/ spell.Main words/small.txt z

echo '\n> Large dictionary test'
# test with no word
java -cp bin/ spell.Main words/words.txt Google

echo '\n> Large dictionary test'
# test with no word
java -cp bin/ spell.Main words/words.txt wefoaijwlifaef

echo '\n> Large dictionary test'
# test with no word
java -cp bin/ spell.Main words/words.txt facebook

echo '\n> End Tests.🍕\n'
