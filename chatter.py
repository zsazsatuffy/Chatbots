#!/usr/bin/env python

# You need to install chatterbot to make this script work
# Install from  https://github.com/gunthercox/ChatterBot  with
#   pip install chatterbot

from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# # Get a response to an input statement
# chatbot.get_response("Hello, how are you today?")

print "Hello, I am Chatterbot"
while True:
    humanSpeak = raw_input("> ")
    botSpeak = chatbot.get_response(humanSpeak)
    print botSpeak
