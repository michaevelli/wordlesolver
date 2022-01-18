## Wordle Solver

Solves the [Wordle](https://www.powerlanguage.co.uk/wordle/) game using a minimax algorithm.  
Word bank obtained from website via inspect element.  

Algorithm is Minimax. It begins with the restricted word bank of possible answers and then chooses a guess such that in the worst case, the most amount of words from the set of valid answers are eliminated as valid answers. If possible, a guess will be chosen that is in the set of possible answers but the optimal guess may not be in that set.

A run of the algorithm with the word bank and possible answers gives the following optimal starting guesses: `ARISE`, `RAISE`, `AESIR` and `SERAI`. Only the first 2 are in the possible word bank so rather than wait 2 hours for a first guess that will always be the same word, `RAISE` is hardcoded as the first guess.
A first pass of the algorithm has been performed for every possible result. The subsequent guess for each result has been stored and is retrieved to reduce execution time (Second guesses typically take around 10 minutes otherwise). A significant number of second guesses are `AAHED` because the result and `RAISE` do not provide any compatible words. Eg, `YYYGG` and `RAISE` do not result in any words in the possible answers word bank. Hence, the code I used to generate second guesses defaulted to the first word in the word bank, `AAHED`. At this point the possible words set is usually around 10 words max which takes the algorithm about 1 minute to execute.

Running the algorithm on all possible words give the following results

| Guesses Required | Occurences | Percentage |
|-----------------:|-----------:|-----------:|
|                1 |          1 |      0.04% |
|                2 |         67 |      2.89% |
|                3 |        953 |     41.17% |
|                4 |       1206 |     52.10% |
|                5 |         88 |      3.80% |
|                6 |          0 |      0.00% |

This gives this algorithm an average case of 3.57 turns to guess the word, with a worst case of 5 turns.


## Usage

I didn't sanitise my inputs, please only input exactly 5 characters per input like `--GY-` where `-` are black, `G` is Green and `Y` is Yellow. 

<pre>
$ <b>python .\solver.py</b>
Guess is RAISE : <b>Y---Y</b>
102 possible words: ['ERROR', 'WOOER', 'GREET', 'GONER', 'HYPER', 'HERON', 'PERCH', 'FERRY', 'QUERY', 'PERKY', 'ELDER', 'ULCER', 'OTHER', 'FEWER', 'FOYER', 'HOMER', 'CREPT', 'EGRET', 'BERTH', 'POWER', 'POKER', 'GRUEL', 'LEERY', 'THREW', 'DETER', 'LOVER', 'UDDER', 'DERBY', 'ERUPT', 'CREEK', 'QUEER', 'FREER', 'FLYER', 'BLUER', 'WRECK', 'COVER', 'JOKER', 'CREED', 'OUTER', 'DEMUR', 'ENTER', 'EVERY', 'OTTER', 'TUBER', 'CREEP', 'BUYER', 'LOWER', 'CYBER', 'OFFER', 'DRYER', 'OVERT', 'ETHER', 'CREDO', 'BOXER', 'PREEN', 'LEMUR', 'BREED', 'NEVER', 'OWNER', 'EMBER', 'HOVER', 'JERKY', 'UPPER', 'MOVER', 'DEFER', 'CRUEL', 'NERDY', 'FREED', 'DECOR', 'UTTER', 'ORDER', 'UNDER', 'CLERK', 'OLDER', 'CHEER', 'GREEN', 'ENTRY', 'VOTER', 'ODDER', 'LEPER', 'TENOR', 'TREND', 'TOWER', 'FEVER', 'TRUER', 'PURER', 'MERRY', 'BERRY', 'COWER', 'ERECT', 'GREED', 'BERET', 'EXERT', 'CORER', 'MOWER', 'METRO', 'NEWER', 'LEVER', 'METER', 'FEMUR', 'DECRY', 'MERCY']
Guess is OUTER : <b>-G-YY</b>
1 possible words: ['QUERY']
Guess is QUERY : <b>GGGGG</b>
Word is QUERY
</pre>

<pre>
$ <b>python .\solver.py
Guess is RAISE : <b>Y-G--</b>
28 possible words: ['PRINT', 'BRING', 'DRINK', 'PRICK', 'CRIMP', 'PRIMO', 'BRINK', 'QUIRK', 'GRIND', 'FRITZ', 'TWIRL', 'PRIVY', 'CRICK', 'THIRD', 'TRICK', 'FLIRT', 'GRILL', 'BRICK', 'BRINY', 'DRILL', 'KRILL', 'FRILL', 'DRIFT', 'PRIOR', 'GRIMY', 'WRING', 'WHIRL', 'CHIRP']
Guess is CLONK : <b>---GG</b>
2 possible words: ['DRINK', 'BRINK']
Guess is DRINK : <b>GGGGG</b>
Word is DRINK
</pre>

## Installation

Python 3.9.1

## Contributing

Do as you wish, I suppose

## License

MIT