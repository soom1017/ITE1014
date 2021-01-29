# hangman game
import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']

# words: from google
# enter_to_space.py로 가독성 있게 정렬하였음.    
words = '''abruptly absurd abyss
affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou
beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo
buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt
curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip
espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness
flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo
giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard
hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk
jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial
joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk
kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis
matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph
onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia
polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz
quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy
sphinx spritz squawk staff strength strengths stretch stronghold stymied subway
swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth
twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex
voyeurism walkway waltz wave wavy waxy wellspring wheezy whiskey whizzing
whomever wimpy witchcraft wizard woozy wristwatch wyvern xylophone yachtsman yippee
yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac zombie'''.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' guesses')
                gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
