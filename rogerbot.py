#!/usr/bin/env python

# Roger bot

import chatServer as c
import random


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


# Setup and Response function
def setup():
    global askedCounter
    global orderCounter
    askedCounter = 0
    orderCounter = 0
    output("Hello, my name is Roger.")
    sleep(1)
    output("What's up?")


def response(input):
    # print(input)
    if respondToTrigger(input):
        pass
    else:
        output(defaultOrderedResponse())


def defaultOrderedResponse():
    answers = [
        "Ok",
        "Roger",
        "Copy that",
        "Confirmative",
        "Okay",
        "Okeydokey",
        "Yes",
        "Sure",
        "I agree",
        "Absolutely"
    ]
    response = answers[orderCounter]
    orderCounter += 1
    if orderCounter >= len(answers):
        orderCounter = 0
    return response


def randomAssignments():
    answers = [
        "The assignment is to design a chatbot.",
        "Design a chatbot",
        "A Chatbot, You make it!",
        "Make it work, this chatbot."
    ]
    return random.choice(answers)


def respondToTrigger(input):
    global askedCounter
    triggers = ["assignment", "opdracht", "what do I do"]
    for t in triggers:
        if t in input:
            if askedCounter > 0:
                output("Why do you ask me this again?")
            output(randomAssignments())
            askedCounter += 1
            return True
    return False
