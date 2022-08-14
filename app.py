from MLEmojiDetectionBot.MLEmoPredict import MLEmoPredict
from ChatBot.ChatBot import GenerateChatBot
from SuggestionBot.MovieSugg import MovieSuggBot
from flask import Flask, render_template, request

from SuggestionBot.MusicSugg import MusicSuggBot

app = Flask(__name__)

availBot = {"chatbot": None, "emojibot": None, "movieSuggbot": None, "musicSuggbot": None}
currBot = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    if botChangeDetect(userText):
        inputProcess(userText)
        return str("<div class='botText'><div>Bot is ready</div></div>")
    else:
        if (currBot == None):
            return "<div class='botText'><div>Wrong command. Please select a bot</div></div>"

        return str(currBot.getResponse(userText))

    return str("If you see this line. It must be some error.")


def botChangeDetect(user):
    if user == "i want to chat" or user == "i want emoji" or user == "i want movie" or user == "i want music":
        return True
    return False


def inputProcess(user):
    global currBot

    if user == "i want to chat":
        if availBot["chatbot"] is None:
            availBot["chatbot"] = GenerateChatBot("randomName")
        currBot = availBot["chatbot"]

    elif user == "i want emoji":
        if availBot["emojibot"] is None:
            availBot["emojibot"] = MLEmoPredict()
        currBot = availBot["emojibot"]

    elif user == "i want movie":
        if availBot["movieSuggbot"] is None:
            availBot["movieSuggbot"] = MovieSuggBot()
        currBot = availBot["movieSuggbot"]

    elif user == "i want music":
        if availBot["musicSuggbot"] is None:
            availBot["musicSuggbot"] = MusicSuggBot()
        currBot = availBot["musicSuggbot"]

    return None


if __name__ == "__main__":
    app.debug = True
    app.run()
