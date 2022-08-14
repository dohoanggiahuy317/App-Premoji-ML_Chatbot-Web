# Premoji - ML Chat Bot App

## Introduce
This projects includes 4 different bots: Chat bot, Feeling detection bot, movie and music suggestion bot. This project uses Flask app to deploy on Web and Chatterbot libraries to train and implement bot use.

![](../../Screen Shot 2022-08-15 at 1.42.47 AM.png)

## Bots
### Chat bot
This bot implements Chatterbot libraries and is trained with Cornell Movie--Dialogs Corpus database. The bot can response to user's input and give definition in certion themes such as soccer, philosophy, or food. This bot can be enhance by feeding it better diaglogs or data.

![](../../../../../var/folders/82/pxqzvdgd0ts9wgxpy3z3ngf00000gn/T/TemporaryItems/NSIRD_screencaptureui_w8MTOZ/Screen Shot 2022-08-15 at 1.52.28 AM.png)

### Feeling detection bot
This bot uses sklearn to learn a pattern from a data set to predict user emotion from their text, and print out the emoji for that feeling. It is trained with SVC, linearSVC, RandomForestClassifier, and DecisionTreeClassifier. The result is taken from the model with highest accuracy. This bot can be improve with better data set and sample.

![](../../Screen Shot 2022-08-15 at 1.50.41 AM.png)

### Movie and Suggestion bot
These 2 bot use selenium and beautifulsoup libraries to parse YouTube and ImDB website. They use user's input as keyword for the searching and retunr the HTML tag with the songs or movies name. This bot can also take the value that is predicted from felling detection bot for searching in order to improve user experience

![](../../../../../var/folders/82/pxqzvdgd0ts9wgxpy3z3ngf00000gn/T/TemporaryItems/NSIRD_screencaptureui_dS7QHA/Screen Shot 2022-08-15 at 1.51.47 AM.png)