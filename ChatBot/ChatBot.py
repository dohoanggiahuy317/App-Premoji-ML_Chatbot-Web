from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import json

class GenerateChatBot:

    chatbot = None

    def __init__(self, name):
        self.chatbot = ChatBot(name, storage_adapter="chatterbot.storage.SQLStorageAdapter")
        print("Training....")
        self.ChatBotTraining()
        print("Done Training")

    def ChatBotTraining(self):
        # trainer = ChatterBotCorpusTrainer(self.chatbot)
        # trainer.train("chatterbot.corpus.english")

        # --------------------------------------------------------------------------------------------------------------
        trainer = ListTrainer(self.chatbot)

        data = self.loadDataSet()
        # Iterating through the json
        for each_dialog in data:
            trainList = []
            for conversation in each_dialog["dialog"]:
                trainList.append(conversation["text"])
            trainer.train(trainList)
        # --------------------------------------------------------------------------------------------------------------

    def loadDataSet(self):
        # Opening JSON file
        f = open('ChatBot/dataChatBot.json')

        # returns JSON object as a dictionary
        data = json.load(f)

        # Closing file
        f.close()

        return data

    def getResponse(self, text):
        return str("<div class='botText'><div>" + str(self.chatbot.get_response(text)) + "</div></div>")