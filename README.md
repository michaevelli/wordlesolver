## Wordle Solver

Solves the [Wordle](https://www.powerlanguage.co.uk/wordle/) game using a minimax algorithm.  
Word bank obtained from website via inspect element.  
Algorithm can take 10 minutes for a second guess (maybe longer), but subsequent guesses are quite fast as the possible words set is reduced.  
Starting guess is always `STEAL` because I am unsure of an optimal first guess. I choose to have a first guess including the letters "E", "T" and "A", being the most common letters of the english language.

## Usage

I didn't sanitise my inputs, please only input exactly 5 characters per input like `--GY-` where `-` are black, `G` is Green and `Y` is Yellow. 

<pre>
$ <b>python .\solver.py
Guess is STEAL : <b>-----</b>
221 possible words: ['HUMPH', 'MIMIC', 'POUND', 'BOOBY', 'IVORY', 'ROUND', 'CIVIC', 'CORNY', 'FJORD', 'DOWRY', 'BOOZY', 'DUCHY', 'GROIN', 'GROUP', 'BRING', 'RHINO', 'CONIC', 'PICKY', 'UNIFY', 'DRINK', 'PROXY', 'PRICK', 'CRIMP', 'WRUNG', 'HUMOR', 'ROBIN', 'CYNIC', 'VIVID', 'MOURN', 'NYMPH', 'FOUND', 'CHUNK', 'FORGO', 'VOUCH', 'DONOR', 'PRIMO', 'BRINK', 'HYDRO', 'ROOMY', 'BOBBY', 'CINCH', 'BUGGY', 'HUNKY', 'WIDOW', 'IRONY', 'FUNGI', 'WHOOP', 'BOUGH', 'VIGOR', 'HOWDY', 'IONIC', 'QUIRK', 'MUMMY', 'FOGGY', 'POOCH', 'HIPPY', 'OPIUM', 'INCUR', 'FUNNY', 'MOUND', 'QUICK', 'GRIND', 'JIFFY', 'WOOZY', 'MUDDY', 'ONION', 'COUCH', 'GOODY', 'FROWN', 'HUMID', 'CROCK', 'BIRCH', 'WINCH', 'CHUMP', 'MORON', 'CROUP', 'JUICY', 'CROOK', 'ICING', 'RIGOR', 'POPPY', 'DOWDY', 'DUMPY', 'HORNY', 'DOING', 'DYING', 'BUDDY', 'CHORD', 'CROWD', 'PRIVY', 'BONGO', 'PUDGY', 'CHOIR', 'CRICK', 'FUROR', 'COUGH', 'FURRY', 'CRUMP', 'DOUGH', 'UNZIP', 'MINOR', 'MURKY', 'BUXOM', 'PORCH', 'DINGO', 'BROOD', 'PIGGY', 'WHICH', 'POUCH', 'CROWN', 'WOODY', 'COMIC', 'FROCK', 'DRUNK', 'PRONG', 'WORRY', 'FINCH', 'GROOM', 'YOUNG', 'FROND', 'OVOID', 'CHUCK', 'PUPPY', 'BUNNY', 'JUMBO', 'CONCH', 'DROOP', 'RUGBY', 'MICRO', 'COMFY', 'GRUFF', 'ROCKY', 'GROWN', 'CUMIN', 'RIGID', 'ROWDY', 'MUCKY', 'BINGO', 'HONOR', 'PHONY', 'BRICK', 'VYING', 'HIPPO', 'RUDDY', 'WINDY', 'CRUMB', 'DUMMY', 'BROOM', 'HOBBY', 'IDIOM', 'CHICK', 'WHINY', 'WHIFF', 'WRONG', 'HUNCH', 'PUFFY', 'CURIO', 'CHURN', 'WIMPY', 'JUROR', 'MORPH', 'MOODY', 'FUZZY', 'CUBIC', 'BRINY', 'BOUND', 'PROUD', 'GUMBO', 'DIZZY', 'BROOK', 'NINNY', 'OWING', 'MINIM', 'ROUGH', 'WORDY', 'FUNKY', 'DINGY', 'PROOF', 'DODGY', 'MYRRH', 'PRIOR', 'PINKY', 'CHOCK', 'FORUM', 'JUMPY', 'GIDDY', 'RUMOR', 'WOUND', 'INBOX', 'FIZZY', 'KINKY', 'GRIMY', 'CURVY', 'BIDDY', 'CURRY', 'OCCUR', 'PUBIC', 'MUNCH', 'HURRY', 'PYGMY', 'WRING', 'DROWN', 'GUPPY', 'UNION', 'DRUID', 'CRONY', 'BUNCH', 'KNOWN', 'PUNCH', 'DOWNY', 'GOOFY', 'GUMMY', 'CHIRP', 'GOURD', 'BROWN', 'PINCH', 'GOING', 'HOUND', 'UNDID', 'KNOCK', 'CONDO']
Guess is ROUND : <b>Y--GY</b>
1 possible words: ['DRINK']
Guess is DRINK : <b>GGGGG</b>
</pre>
## Installation

Python 3.9.1

## Contributing

Do as you wish, I suppose

## License

MIT