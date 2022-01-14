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

# Get word bank
f = open("wordbank.txt")
wordBank = f.read().split(" ")
f.close()
f = open("wordbankanswers.txt")
possible = f.read().split(" ")
f.close()

# Prepare lists
scores = []
for i in range(len(wordBank)):
    scores += [0]

f = open("possibleresults.txt")
possibleResults = f.read().split(" ")
f.close()

guess = "RAISE"

for j in range(1, len(possibleResults)):

    result = possibleResults[j]

    print(str(j) + ": " + result)

    #prune possible words
    tempPossible = []
    for word in possible:
        testResult = query(word, guess)
        if result == testResult:
            tempPossible += [word]
    
    for i in range(len(wordBank)):
        word = wordBank[i]
        scores[i] = len(wordBank)
        for possibleresult in possibleResults:
            countmin = 0
            for possibleword in tempPossible:
                possiblewordresult = query(possibleword, word)
                if possiblewordresult != possibleresult:
                    countmin += 1
            if scores[i] > countmin:
                scores[i] = countmin
    
    # Guess the Max of the Min
    highscores = [i for i, j in enumerate(scores) if j == max(scores)]
    guess = wordBank[scores.index(max(scores))]

    # try to use a guess in the possible set
    for i in highscores:
        if wordBank[i] in tempPossible:
            guess = wordBank[i]
            break
    
    print(guess)
    f = open("a.out", "a")
    f.write(guess)
    f.write(" ")
    f.close()
    guess = "RAISE"