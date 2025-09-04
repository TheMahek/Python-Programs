import random
word_bank = ['Apple', 'Ocean', 'Happy', 'Mountain', 'Music','Book']
word = random.choice(word_bank).lower()
guessedWord = ['_'] * len(word)
attempts = 10
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()
   
  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
    print('Great guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))
  if '_' not in guessedWord:
    print('\n🎉 Congratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedWord:
  print('\n😢 You\'ve run out of attempts! The word was: ' + word)

