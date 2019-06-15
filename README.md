# cr-upgrade-calculator-v2
Working on a fully automated calculator that shows useful stats of a deck in Clash Royale. To improve my calculator from March. 
Version 1 can be found [here](https://studio.code.org/projects/applab/cKkV1c9y037xD3tObsSR8IUf3ciuh4h5CJ-gOiFRkus)

## About
In a mobile game called Clash Royale, you play battles against other players with the use of a deck of cards. Each card has it's own stats and personality. In particular, the levels and amount of cards acquired. A card's strength is indicative by the level, and the higher level a card is the stronger it gets. To level up a card, you need two things: Gold and a certain amount of cards. For the past few months, I've been theorycrafting what decks I could realistically make that can be of max level, where they are at their strongest and I can viably use them against other players. I'd usually figure out how realistic these decks are to make (meaning I can afford the resource of Gold, amount of cards, and especially time) by hand by having tables of gold upgrade costs per level, card amount costs per level, and estimated time to collect certain amounts of cards open on my screen while I have a calculator. This would usually take me 6-8 minutes. I did get the job done, but it was tedious and I felt like I could work out my programming muscles on this. I first made the calculator in code.org's App Lab, which is based in JavaScript but does have the perk of having an easy to make UI. Now that I'm in summer break and learning Python, I feel the need to return to this and improve on it. I'll go more in-depth about them in the next topics. 

## Stats
So what can a deck tell us?
Well, we can see for each card:
* Name
* Level
* Card Amount

There are more stats but these are the ones of focus. With this, we can then infer:
* The cost to upgrade a card to a certain level
* The amount of cards needed to upgrade a card to a certain level
* The estimated time it will take to get the necessary resources (gold, amount of cards) to upgrade a card to a certain level.

## Features of v1.x
* Shows 8 deck slots, each to be inputted a card name, card level, and card amount
* A button for starting the calculation
* A print screen at the bottom displaying necessary cost, amount, and estimated time for each card to max out (get upgraded to the max level) as well as the whole deck
* Later changes added an options menu but was flawed
* JavaScript (code.org App Lab)

## v2.0: Improvements over v1.x
* It can make use of Clash Royale's API (made a dev account!) and completely eliminate the need to manually enter in deck data.
* It can calculate decks for levels besides max. (level 13)
* It may be implemented into its own website one day... (can learn HTML and CSS from freecodecamp)
* For now, it'll be something to be ran in command line. Oh well
* Python
