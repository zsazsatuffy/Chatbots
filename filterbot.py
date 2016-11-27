#!/usr/bin/env python

# Filter bot

import chatServer as c
import random


# Sleep and output functions
def sleep(n):
    c.sleep(n)


def output(s):
    c.output(s)


# Setup and Response function
def setup():
    output("Hello, this is the filterbot")


def response(input):
    # print(input)
    if respondToGreeting(input):
        pass
    elif respondToFood(input):
        pass
    elif respondToWeather(input):
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
    response = random.choice(answers)
    return response


def randomGreetings():
    answers = [
        "Hello",
        "Hi.",
        "What's up?",
        "Yo."
    ]
    return random.choice(answers)


def randomWeather():
    answers = [
        "It's nice today, isn't it?",
        "Less rain than yesterday",
        "I like the summer",
        "Will the sun come back?"
    ]
    return random.choice(answers)


def randomFood():
    answers = [
        "Did you have lunch already?",
        "Let's have dinner this week.",
        "Do you also like cucumbers?",
        "I'm hungry"
    ]
    return random.choice(answers)


def respondToGreeting(input):
    triggers = ["hello", "hi", "how are you"]
    for t in triggers:
        if t in input:
            output(randomGreetings())
            return True
    return False


def respondToWeather(input):
    triggers = ["weather", "warm", "cold", "rain", "nice"]
    for t in triggers:
        if t in input:
            output(randomWeather())
            return True
    return False


def respondToFood(input):
    triggers = ["food", "eat", "ate", "dinner", "lunch", "breakfast"]
    for t in triggers:
        if t in input:
            output(randomFood())
            return True
    return False
