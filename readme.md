### Premoji - ML Chat Bot App

## Introduce
This projects includes 4 different bots: Chat bot, Feeling detection bot, movie and music suggestion bot. This project uses Flask app to deploy on Web and Chatterbot libraries to train and implement bot use.

## Bots
# Chat bot
This bot implements Chatterbot libraries and is trained with Cornell Movie--Dialogs Corpus database. The bot can response to user's input and give definition in certion themes such as soccer, philosophy, or food. This bot can be enhance by feeding it better diaglogs or data.

# Feeling detection bot
This bot uses sklearn to learn a pattern from a data set to predict user emotion from their text, and print out the emoji for that feeling. This bot can be improve with better data set and sample.

# Movie and Suggestion bot
These 2 bot use selenium and beautifulsoup libraries to parse YouTube and ImDB website. They use user's input as keyword for the searching and retunr the HTML tag with the songs or movies name. This bot can also take the value that is predicted from felling detection bot for searching in order to improve user experience
