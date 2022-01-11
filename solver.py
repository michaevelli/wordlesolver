def splitString(s):
    return [c for c in s]


def query(answer, guess):
    result = ["-", "-", "-", "-", "-"]
    answerlist = splitString(answer)
    guesslist = splitString(guess)
    for i in range(len(guesslist)):
        if guesslist[i] == answerlist[i]:
            result[i] = "G"
            answerlist[i] = " "
    for i in range(len(guesslist)):
        if result[i] == "G":
            continue
        if guesslist[i] in answerlist:
            result[i] = "Y"
            answerlist[answerlist.index(guesslist[i])] = " "
    return "".join(result)  
        



# Word list from https://www.bestwordlist.com/5letterwords.htm
f = open("wordbankanswers.txt")
wordBank = f.read().split(" ")
possible = wordBank[:]
f.close()

scores = []
for i in range(len(wordBank)):
    scores += [0]

oldguesses = []

f = open("possibleresults.txt")
possibleResults = f.read().split(" ")
f.close()

# No doubt there is an optimal first guess but I settled for 5 distinct characters, containing T, E, A (most frequent english letters)
guess = "STEAL"
oldguesses += [guess]
result = input("Guess is " + guess + " : ").upper()

while (result != "GGGGG"):
    # Prune possible words
    tempPossible = []
    for word in possible:
        testResult = query(word, guess)
        if result == testResult:
            tempPossible += [word]
    possible = tempPossible
    
    print(str(len(possible)) + " possible words: " + str(possible))

    # MinMax
    for i in range(len(wordBank)):
        word = wordBank[i]
        if word in oldguesses:
            scores[i] = 0
            continue
        scores[i] = len(wordBank)
        for possibleresult in possibleResults:
            countmin = 0
            for possibleword in possible:
                possiblewordresult = query(possibleword, word)
                if possiblewordresult != possibleresult:
                    countmin += 1
            if scores[i] > countmin:
                scores[i] = countmin
    
    # Guess the Max of the Min
    highscores = [i for i, j in enumerate(scores) if j == max(scores)]

    guess = wordBank[scores.index(max(scores))]

    for i in highscores:
        if wordBank[i] in possible:
            guess = wordBank[i]
            break
    
    oldguesses += [guess]
    result = input("Guess is " + guess + " : ")





