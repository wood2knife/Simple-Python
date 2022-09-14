import random

print("""
╔╗─╔╗╔═══╗╔═╗─╔╗╔═══╗╔═╗╔═╗╔═══╗╔═╗─╔╗
║║─║║║╔═╗║║║╚╗║║║╔═╗║║║╚╝║║║╔═╗║║║╚╗║║
║╚═╝║║║─║║║╔╗╚╝║║║─╚╝║╔╗╔╗║║║─║║║╔╗╚╝║
║╔═╗║║╚═╝║║║╚╗║║║║╔═╗║║║║║║║╚═╝║║║╚╗║║
║║─║║║╔═╗║║║─║║║║╚╩═║║║║║║║║╔═╗║║║─║║║
╚╝─╚╝╚╝─╚╝╚╝─╚═╝╚═══╝╚╝╚╝╚╝╚╝─╚╝╚╝─╚═╝
""")
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = "ant baboon badger bat bear beaver camel cat clam cobra cougar\
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk\
lion lizard llama mole monkey moose mouse mule newt otter owl panda\
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep\
skunk sloth snake spider stork swan tiger toad trout turkey turtle\
weasel whale wolf wombat zebra".split()
random.seed()
repeat_letters = []
user_input = input('Type any letter(s) to play the game or "exit" to quit: ')
while user_input != "exit":
    word = random.choice(words)
    word_length = len(word)
    hint = ["-"] * word_length
    count_hint = len(hint)
    attemps = 8
    while attemps > 0 and count_hint > 0:
        print()
        print("".join(hint))
        guess = input("Input a letter: ")
        if len(guess) >= 2 or len(guess) == 0:
            print("You should input a single letter")
        elif (ord(guess) < 97) or (ord(guess) > 122):
            print("Please enter a lowercase English letter")
        elif guess in repeat_letters:
            print("You've already guessed this letter")
        elif guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    if hint[i] == "-":
                        hint[i] = guess
                        count_hint -= 1
                    else:
                        print("You've already guessed this letter")
                        break
        else:
            print("That letter doesn't appear in the word")
            print(HANGMANPICS[8 - attemps])
            attemps -= 1
        repeat_letters.append(guess)
    if attemps == 0:
        print("You lost!")
    if count_hint == 0:
        print()
        print("You won!")
        print("The word was --", word)
    print()
    user_input = input('Type any letter to play the game, "exit" to quit: ')
