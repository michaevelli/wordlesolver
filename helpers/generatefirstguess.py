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

oldguesses = []

f = open("possibleresults.txt")
possibleResults = f.read().split(" ")
f.close()


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

# print indicies of optimal starting guesses
print(highscores)

# try to use a guess in the possible set
for i in highscores:
    if wordBank[i] in possible:
        guess = wordBank[i]
        break

oldguesses += [guess]
result = input("Guess is " + guess + " : ")





