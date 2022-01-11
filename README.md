## Wordle Solver

Solves the [Wordle](https://www.powerlanguage.co.uk/wordle/) game using a minimax algorithm.  
Word bank obtained from website via inspect element.  
Algorithm can take 10 minutes for a second guess (maybe longer), but subsequent guesses are quite fast as the possible words set is reduced.  
A run of the algorithm with the word bank and possible answers gives the following optimal starting guesses: `ARISE`, `RAISE`, `AESIR` and `SERAI`. Only the first 2 are in the possible word bank so rather than wait 2 hours for a first guess that will always be the same word, `RAISE` is hardcoded as the first guess.

## Usage

I didn't sanitise my inputs, please only input exactly 5 characters per input like `--GY-` where `-` are black, `G` is Green and `Y` is Yellow. 

<pre>
$ <b>python .\solver.py</b>
Guess is RAISE : <b>Y---Y</b>
102 possible words: ['ERROR', 'WOOER', 'GREET', 'GONER', 'HYPER', 'HERON', 'PERCH', 'FERRY', 'QUERY', 'PERKY', 'ELDER', 'ULCER', 'OTHER', 'FEWER', 'FOYER', 'HOMER', 'CREPT', 'EGRET', 'BERTH', 'POWER', 'POKER', 'GRUEL', 'LEERY', 'THREW', 'DETER', 'LOVER', 'UDDER', 'DERBY', 'ERUPT', 'CREEK', 'QUEER', 'FREER', 'FLYER', 'BLUER', 'WRECK', 'COVER', 'JOKER', 'CREED', 'OUTER', 'DEMUR', 'ENTER', 'EVERY', 'OTTER', 
'TUBER', 'CREEP', 'BUYER', 'LOWER', 'CYBER', 'OFFER', 'DRYER', 'OVERT', 'ETHER', 'CREDO', 'BOXER', 'PREEN', 'LEMUR', 'BREED', 'NEVER', 'OWNER', 'EMBER', 'HOVER', 'JERKY', 'UPPER', 'MOVER', 'DEFER', 'CRUEL', 'NERDY', 'FREED', 'DECOR', 'UTTER', 'ORDER', 'UNDER', 'CLERK', 'OLDER', 'CHEER', 'GREEN', 'ENTRY', 'VOTER', 'ODDER', 'LEPER', 'TENOR', 'TREND', 'TOWER', 'FEVER', 'TRUER', 'PURER', 'MERRY', 'BERRY', 'COWER', 'ERECT', 'GREED', 'BERET', 'EXERT', 'CORER', 'MOWER', 'METRO', 'NEWER', 'LEVER', 'METER', 'FEMUR', 'DECRY', 'MERCY']
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