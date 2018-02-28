import string
def isWordGuessed(secretWord,lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False

    return True

def getGuessedWord(secretWord,lettersGuessed):
    ans=''
    for i in secretWord:
        if i in lettersGuessed:
            ans+=i
        else:
            ans+='_ '

    return ans

def getAvailableLetters(lettersGuessed):
    s = string.ascii_lowercase
    ans=''
    for i in s:
        if i not in lettersGuessed:
            ans+=i

    return ans

def hangman(secretWord):
    lettersGuessed=[]
    mistakesMade=0
    availableLetters=string.ascii_lowercase

    prev_word=getGuessedWord(secretWord,lettersGuessed)
    print(prev_word)
    while(not isWordGuessed(secretWord,lettersGuessed)):
        guess = input('Guess a letter : ')
        guessInLowerCase = guess.lower()
        if guessInLowerCase not in availableLetters:
            print('Already guessed ',guess,'-So try again!')
            continue

        lettersGuessed.append(guessInLowerCase)
        availableLetters=getAvailableLetters(lettersGuessed)
        word = getGuessedWord(secretWord,lettersGuessed)
        print(word)
        if prev_word==word:
            mistakesMade+=1
        prev_word=word

    print('Secret Word : ',word)
    print('Mistakes Made : ',mistakesMade)
