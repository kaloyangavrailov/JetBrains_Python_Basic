import random
random.seed()

tries = 0



words_list = ['python', 'java', 'swift', 'javascript']



letters_tried = set()

games_won = 0

games_lost = 0

game_menu = True
print(f'H A N G M A N')
while game_menu:
    game_menu = False

    action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if action == 'play':
        word = words_list[random.randint(0, 3)]

        hidden_word = list('-' * len(word))
        while tries < 8:
            print()
            print(''.join(hidden_word))
            guess = input('Input a letter: ')
            if len(guess) > 1 or len(guess) < 1 :
                print(f'Please, input a single letter.')
                continue
            elif not guess.islower() or not guess.isalpha():
                print(f'Please, enter a lowercase letter from the English alphabet.')
                continue
            if guess in letters_tried:
                print(f"You've already guessed this letter.")
                continue

            if guess in word and guess not in letters_tried:
                letters_tried.add(guess)
                for n in range(len(word)):
                    if guess == word[n]:
                        hidden_word[n] = guess
                        continue
            elif guess not in word:
                print(f"That letter doesn't appear in the word.")
                tries += 1
                letters_tried.add(guess)
                continue

            if '-' not in hidden_word:
                print(word)
                print(f'You guessed the word {word}!')
                print(f'You survived!')
                letters_tried = set()
                games_won += 1
                game_menu = True
                tries = 0
                break
        if tries == 8:
            print()
            print(f'You lost!')
            letters_tried = set()
            games_lost += 1
            tries = 0
            game_menu = True

    if action == 'results':
        print(f'You won: {games_won} times')
        print(f'You lost: {games_lost} times')
        game_menu = True
        continue
    if action == 'exit':
        break
    else:
        game_menu = True
        continue
