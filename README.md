# bufo-text-interpolation
## How to use
are you overwhelmed by the opportunity abundant in bufo emoji land? simply run 

```
python3 src/main.py <phrase> <N>
```

And you shall receive a list of N suggestions for your string inputted phrase. Note: there are lots of things about installing the appropriate libraries that you might have to do. Sorry, I didn't venv !! 

## Notes: 
Still experimenting with fixing doc similarity. Your current results may be pretty ridiculous, so be warned. Remains to be seen if randomly returned bufos will be more or less matching than suggestions via this bufo-bot

## Examples
Example usage: 

```
python3 src/main.py "an apple a day keeps the doctor away" 10
```

Example output: 
```
*******

For 'an apple a day keeps the doctor away', we recommend bufos:
bufo-offers-an-egg-in-this-trying-time
bufo-gets-hit-in-the-face-with-an-egg
bufo-brings-a-new-meaning-to-brain-freeze-by-bopping-you-on-the-head-with-a-popsicle
it-takes-a-bufo-to-know-a-bufo
bufo-offers-you-a-monster-early-in-the-morning
bufo-offers-you-an-urgent-ticket
bufo-watches-from-a-distance
bufo-just-finished-a-workout
bufo-looks-a-little-closer
bufo-heralds-an-incident
```
