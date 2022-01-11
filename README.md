## Wordle Solver

Solves the [Wordle](https://www.powerlanguage.co.uk/wordle/) game using a minimax algorithm.  
Word bank obtained from [bestwordlist](https://www.bestwordlist.com/5letterwords.htm). I'm not sure if it's the real word bank or not but it contains over 12k words.  
Algorithm can take 10 minutes for a second guess (maybe longer), but subsequent guesses are quite fast as the possible words set is reduced.  
Starting guess is always `STEAL` because I am unsure of an optimal first guess. I choose to have a first guess including the letters "E", "T" and "A", being the most common letters of the english language.

## Usage

I didn't sanitise my inputs, please only input exactly 5 characters per input in the form of `--GY-` where `-` are black, `G` is Green and `Y` is Yellow. 

<pre>
$ <b>python solver.py</b>
Guess is STEAL : <b>--G--</b>
139 possible words: ['BEECH', 'BEEDI', 'BEEFY', 'BEERY', 'BOEUF', 'BREDE', 'BREED', 'BREEM', 'BREER', 'BREID', 'BREME', 'BRERE', 'BREVE', 'CHECK', 'CHEEK', 'CHEEP', 'CHEER', 'CHEMO', 'CHERE', 'CHEVY', 'CHEWY', 'CREDO', 'CREED', 'CREEK', 'CREEP', 'CREME', 'CREPE', 'CREPY', 'CREWE', 'DEEDY', 'DEERE', 'DEEVE', 'DIENE', 'DRECK', 'DREED', 'DRERE', 'DWEEB', 'EMEER', 'EMEND', 'EMERY', 'ENEMY', 'EVERY', 'EXEEM', 'EXEME', 'FEEZE', 'FIEND', 'FIERE', 'FIERY', 'FOEHN', 'FREED', 'FREER', 'FREMD', 'FREON', 'FRERE', 'FUERO', 'GEEKY', 'GREBE', 'GRECE', 'GREED', 'GREEK', 'GREEN', 'GREGE', 'GREGO', 'GREIN', 'GRENZ', 'GREVE', 'HEEDY', 'HEEZE', 'INERM', 'KEECH', 'KEENO', 'KEEVE', 'KIEVE', 'KNEED', 'KREEP', 'KRENG', 'KREWE', 'MIEVE', 'MNEME', 'NEEDY', 'NEEMB', 'NEEZE', 'NIECE', 'NIEVE', 'ODEON', 'ODEUM', 'ONERY', 'OPEPE', 'OXEYE', 'OZEKI', 'PEECE', 'PEEOY', 'PEEPE', 'PEERY', 'PEEVE', 'PHEER', 'PHENE', 'PHEON', 'PIECE', 'PIEND', 'PIEZO', 'PREDY', 'PREED', 'PREEN', 'PREIF', 'PREMY', 'PREOP', 'PREVE', 'PREXY', 'QUEEN', 'QUEER', 'QUEME', 'QUERN', 'QUERY', 'QUEUE', 'QUEYN', 'REECH', 'REEDE', 'REEDY', 'REEFY', 'REEKY', 'REEVE', 'RHEME', 'RHEUM', 'RIEVE', 'UPEND', 'UREDO', 'UREIC', 'VEERY', 'VIEWY', 'WEEDY', 'WEEKE', 'WEENY', 'WEEPY', 'WHEEN', 'WHEEP', 'WHERE', 'WRECK', 'YFERE']
Guess is DEERE : <b>--GG-</b>
6 possible words: ['FIERY', 'FUERO', 'INERM', 'ONERY', 'QUERN', 'QUERY']
Guess is ALOIN : <b>-----</b>
1 possible words: ['QUERY']
Guess is QUERY : <b>GGGGG</b>
</pre>
## Installation

Python 3.9.1

## Contributing

Do as you wish, I suppose

## License

MIT