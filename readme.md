# Premoji - ML Chat Bot App

## Introduce
This projects includes 4 different bots: Chat bot, Feeling detection bot, movie and music suggestion bot. This project uses Flask app to deploy on Web and Chatterbot libraries to train and implement bot use.

<img width="1000" alt="Screen Shot 2022-08-14 at 1 02 28 AM" src="https://user-images.githubusercontent.com/72744045/184551030-87234052-3e3b-4e99-86de-ce5d6624c004.png">


## Bots
### Chat bot
This bot implements Chatterbot libraries and is trained with Cornell Movie--Dialogs Corpus database. The bot can response to user's input and give definition in certion themes such as soccer, philosophy, or food. This bot can be enhance by feeding it better diaglogs or data.

<img width="810" alt="Screen Shot 2022-08-15 at 1 55 44 AM" src="https://user-images.githubusercontent.com/72744045/184551036-02c9c8ba-c110-43e4-99fe-bf99a2f7cbe3.png">

### Feeling detection bot
This bot uses sklearn to learn a pattern from a data set to predict user emotion from their text, and print out the emoji for that feeling. It is trained with SVC, linearSVC, RandomForestClassifier, and DecisionTreeClassifier. The result is taken from the model with highest accuracy. This bot can be improve with better data set and sample.

<img width="734" alt="Screen Shot 2022-08-15 at 1 50 41 AM" src="https://user-images.githubusercontent.com/72744045/184551053-d7742439-d33d-4ea3-a2e2-ed76a56ef897.png">

### Movie and Suggestion bot
These 2 bot use selenium and beautifulsoup libraries to parse YouTube and ImDB website. They use user's input as keyword for the searching and retunr the HTML tag with the songs or movies name. This bot can also take the value that is predicted from felling detection bot for searching in order to improve user experience

<img width="814" alt="Screen Shot 2022-08-15 at 1 55 52 AM" src="https://user-images.githubusercontent.com/72744045/184551059-f7419314-2446-4c46-9d0d-1461b55ea4c6.png">
