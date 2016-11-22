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
    output("Hello, my name is Roger.")
    sleep(1)
    output("What's up?")


def response(input):
    # print(input)
    if not respondToTrigger(input):
        output(randomResponse())


def randomResponse():
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
    return random.choice(answers)


def respondToTrigger(input):
    if "assignment" in input:
        output("The assigment is to design a chatbot.")
        return True
    return False
